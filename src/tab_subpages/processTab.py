import io
import boto3
import pandas as pd
import streamlit as st
import util.constants as const
import util.aws_utils.bedrock_util as bu
import util.aws_utils.smjs_util as su
import time

def process(tab):
    if tab.button('Process Refresh'):
        st.session_state.messages = []
        st.experimental_rerun()

    df = pd.DataFrame({"Files":const.listFiles(const.output_bucket, const.output_dump)})
    option = tab.selectbox("Select File", df, key="processTabBox")
    if not option:
        return False

    tab.divider()
    
    option_llm = tab.selectbox("Select LLM", const.llm_dict.keys(), key="processTabBoxLLM")
    
    tab.divider()
    session = boto3.Session()
    s3 = session.client('s3', region_name=const.region_name)
    data = s3.get_object(Bucket=const.output_bucket, Key=option)
    content = data['Body'].read().decode()
    textArea = tab.text_area("Input Context", value=content, height=200, key="processTabArea")
    tab.divider()

    c1 = tab.container()
    for message in st.session_state.messages:
        chat = c1.chat_message(message["role"])
        chat.markdown(message["content"])

    if (option_llm not in ["Claude V1", "Claude V2", "Claude V2.1", "Claude Instant"]):
        txtInput = tab.text_input("Ask something?", key="processTabInput")
        if txtInput:
            st.session_state.messages.append({"role": "user", "content": txtInput})
            chat = c1.chat_message("user")
            chat.markdown(txtInput)
            
            content = textArea
            prompt = "Context: " + content + "\n" + txtInput
            with st.spinner('processing...'):
                if (option_llm == "Jurassic-2 Mid"):
                    response = bu.call_model_jurassic(prompt, const.llm_dict[option_llm])
                elif (option_llm == "Jurassic-2 Ultra"):
                    response = bu.call_model_jurassic(prompt, const.llm_dict[option_llm])
                elif (option_llm == "Titan Text G1 - Express"):
                    response = bu.call_titan(prompt, const.llm_dict[option_llm])
                # NEED USE CASES TO GET CLAUDE ACCESS
                # elif (option_llm == "Calude V1"):
                #     response = bu.call_model_claude(prompt, const.llm_dict[option_llm])
                # elif (option_llm == "Claude V2"):
                #     response = bu.call_model_claude(prompt, const.llm_dict[option_llm])
                # elif (option_llm == "Claude V2.1"):
                #     response = bu.call_model_claude(prompt, const.llm_dict[option_llm])
                # elif (option_llm == "Claude Instant"):
                #    response = bu.call_model_claude(prompt, const.llm_dict[option_llm])
                elif (option_llm == "Llama 2 Chat 13B"):
                    response = bu.call_model_llama(prompt, const.llm_dict[option_llm])
                elif (option_llm == "Llama 2 Chat 70B"):
                    response = bu.call_model_llama(prompt, const.llm_dict[option_llm])
                else :
                    return
                    
            response = const.escape_str(response)
            chat = c1.chat_message("assistant")
            chatPlaceholder = chat.empty()
            chatResponse = ""
            # Simulate stream of response with milliseconds delay
            for chunk in response.split():
                chatResponse += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                chatPlaceholder.markdown(chatResponse + "▌")

            chatPlaceholder.markdown(chatResponse)
            # Add user message to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        tab.markdown("{0} is not available for this demo. Please select a different LLM.".format(option_llm))
    
