# Ask-PDF

## What is Ask-PDF?

Ask-PDF is a HuggingFace Pipeline powered PDF analyzer and QnA Bot. It is based on Streamlit.

[Source Code](https://github.com/huggingface/transformers/blob/v4.38.2/src/transformers/pipelines/text2text_generation.py#L25)

---

## How to run the code?

Create a Virtual Environment:

```
# If the path is not in the project:
cd {path of the project}

# Creating a virtual environment (myenv is the name of the venv)
python -m venv myenv

# Activating the venv
myenv\Scripts\activate
```

Install the required dependencies:

```
pip install -r requirements.txt
```

Starting the Streamlit app:

```
streamlit run main.py
```

The app opens up in the browser:

* Upload the PDF
* Ask questions regarding the PDF in the text box.

Deactivating the Virtual Environment:

```
myenv\Scripts\deactivate
```

---
