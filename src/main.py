import streamlit as st
import boto3
import botocore
import tab_subpages.inputTab as inputTab
import tab_subpages.processTab as processTab
import tab_subpages.translateTab as translateTab
import tab_subpages.comprehendTab as comprehendTab
import tab_subpages.crawlTab as crawlTab
import util.page_utils.auth_util as auth_util
import util.page_utils.session_utils as session_utils

if not auth_util.check_password():
    st.stop()

inputT, processT, translateT, comprehendT, crawlT = st.tabs(["Input", "GenAI", "Translate", "Comprehend", "Web"])

session_utils.init_session_state()

inputTab.uploader(inputT)
processTab.process(processT)
translateTab.translate(translateT)
comprehendTab.process(comprehendT)
crawlTab.process(crawlT)
