## aws-bedrock-streamlit-poc-: 
Using Streamlit to talk to various AWS AI and ML Services

This example uses streamlit to demonstrate some basic user interfaces. It allows the user to:
1. Upload single-page PDFs into S3
2. Convert PDF into text and store in an output bucket
3. bedrock (various models, selectable) to do LLM text processing on the output files
4. translate uploaded and converted files with AWS Translate
5. some basic entity recognition and PII extraction via AWS Comprehend on converted files
6. Use googlesearch python package to download webpage contents, using Bedrock for summarization and Comprehend for sentiment analysis

## Getting Started
1. Install python3.8 or higher
2. Install AWS CLI
3. Note that Streamlit runs on port 8501

Clone this repository:
```
'git clone wherethisshouldbehosted.com'
```

Download libraries & setup a virtual environment so all python dependencies are stored within project directory:
```
Admin:~/environment/aws-bedrock-streamlit-poc (main) $ ./download-dependencies.sh
Admin:~/environment/aws-bedrock-streamlit-poc (main) $ python -m venv .venv
Admin:~/environment/aws-bedrock-streamlit-poc (main) $ source .venv/bin/activate
(.venv) Admin:~/environment/aws-bedrock-streamlit-poc (main) $ pip install -r requirements.txt
```

Create a directory and file to store global password for the steamlit application:
```
Admin:~/environment/aws-bedrock-streamlit-poc (main) $ less .streamlit/secrets.toml

# .streamlit/secrets.toml

password = "Your-Password"
```

Update resources in the constants.py file:
```
input_bucket = "poc-input"
output_bucket = "poc-output"
bedrock_ep_url = "bedrock-endpoint-url"
region_name = "us-east-1"
```

Ensure that the Role/permissions associated with your local setup can access:
1. Required S3 buckets
2. Textract, Translate, Comprehend and Bedrock services

## Now we run the sample streamlit application
To run the streamlit application, run the following command:
```
(.venv) Admin:~/environment/aws-bedrock-streamlit-poc (master) $ streamlit run src/main.py 

Collecting usage statistics. To deactivate, set browser.gatherUsageStats to False.


  You can now view your Streamlit app in your browser.

  Network URL: http://a.b.c.e:8501
  External URL: http://w.x.y.z:8501
```

There are some sample single-page PDF files to try:
```
Admin:~/environment/aws-bedrock-streamlit-poc (master) $ ls pdf-samples/
bank-statement.pdf  payslip.pdf cpi_nov_2023_summary.pdf

cpi_nov_2023.pdf is not single page, so it won't yet work.
```
