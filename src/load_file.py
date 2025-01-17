import requests
import streamlit as st
from tempfile import NamedTemporaryFile
from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader

####################### Function for loading and caching the content of the PDF file #######################
@st.cache_data
def load_pdf_content(user_manuel_url):

    # Download the PDF from the URL and save it temporarily
    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        response = requests.get(user_manuel_url)
        tmp_file.write(response.content)
        tmp_file_path = tmp_file.name

    # Load the PDF content using PyPDFLoader
    pdf_loader = PyPDFLoader(tmp_file_path)
    pdf_reader = pdf_loader.load()
    
    # Extract and format the content
    content = [(page.page_content.replace('\n', '\n\n')
                if page.page_content else '...') for page in pdf_reader]
    return content

def load_url_content():
    # Load the web page content
    with st.spinner('Loading PDF content. Please wait around a minute...'):
        loader = WebBaseLoader(["https://docs.digitalocean.com/products/app-platform/", "https://docs.digitalocean.com/products/app-platform/getting-started/quickstart/"
                            "https://docs.digitalocean.com/products/app-platform/how-to/create-apps/", "https://docs.digitalocean.com/products/app-platform/how-to/deploy-from-container-images/", "https://docs.digitalocean.com/products/app-platform/how-to/deploy-from-monorepo/",
                            "https://docs.digitalocean.com/products/app-platform/how-to/scale-app/", "https://docs.digitalocean.com/products/app-platform/how-to/add-deploy-do-button/", "https://docs.digitalocean.com/products/app-platform/how-to/manage-components/", "https://docs.digitalocean.com/products/app-platform/how-to/manage-services/", "https://docs.digitalocean.com/products/app-platform/how-to/manage-jobs/", "https://docs.digitalocean.com/products/app-platform/how-to/manage-workers/",
                            "https://docs.digitalocean.com/products/app-platform/how-to/manage-static-sites/", "https://docs.digitalocean.com/products/app-platform/how-to/manage-functions/", "https://docs.digitalocean.com/products/app-platform/how-to/manage-data-storage/",
                            "https://docs.digitalocean.com/products/app-platform/how-to/manage-databases/", "https://docs.digitalocean.com/products/app-platform/details/limits/", "https://docs.digitalocean.com/products/app-platform/how-to/build-run-commands/", "https://docs.digitalocean.com/products/app-platform/how-to/use-environment-variables/"
                            "https://docs.digitalocean.com/products/app-platform/how-to/cache-content/", "https://docs.digitalocean.com/products/app-platform/how-to/change-region/", "https://docs.digitalocean.com/products/app-platform/how-to/change-stack/",
                            "https://docs.digitalocean.com/products/app-platform/how-to/upgrade-buildpacks/", "https://docs.digitalocean.com/products/app-platform/how-to/manage-time-zone/", "https://docs.digitalocean.com/products/app-platform/how-to/add-ip-address/",
                            "https://docs.digitalocean.com/products/app-platform/how-to/manage-domains/", "https://docs.digitalocean.com/products/app-platform/how-to/configure-cors-policies/", "https://docs.digitalocean.com/products/app-platform/how-to/manage-internal-routing/",
                            "https://docs.digitalocean.com/products/app-platform/how-to/url-rewrites/", "https://docs.digitalocean.com/products/app-platform/how-to/manage-health-checks/", "https://docs.digitalocean.com/products/app-platform/how-to/view-logs/", "https://docs.digitalocean.com/products/app-platform/how-to/forward-logs/",
                            "https://docs.digitalocean.com/products/app-platform/how-to/create-alerts/", "https://docs.digitalocean.com/products/app-platform/how-to/view-insights/",
                            "https://docs.digitalocean.com/products/app-platform/how-to/manage-deployments/", "https://docs.digitalocean.com/products/app-platform/how-to/update-app-spec/", "https://docs.digitalocean.com/products/app-platform/how-to/manage-source-repo/", "https://docs.digitalocean.com/products/app-platform/how-to/build-locally/", "https://docs.digitalocean.com/products/app-platform/how-to/destroy-app/"])

        loader.requests_per_second = 1
        docs = loader.load()
        
        
        return docs

###########################################################################################################
########################### Function for displaying the PDF file and the images ###########################
###########################################################################################################
def load_file():
    
    user_manuel_url = 'https://raw.githubusercontent.com/Samuelchazy/Educative.io/badc624f25a17ef9c36400d4dbc7f2f1275ba21c/user_manuel/Toyota-Highlander-2024.pdf'

    with st.spinner('Loading PDF content. Please wait around a minute...'):
        content = load_pdf_content(user_manuel_url)

    if content:

        with st.container(height=600, border=False):
            col_left, col_right = st.columns(2)

            ###################################### Display the images #####################################
            with col_left:
                image_path = "https://raw.githubusercontent.com/Samuelchazy/Educative.io/19d3100db50749489689a5c21029c3499722b254/images/Toyota_3.jpg"
                st.image(image_path, use_column_width=True)

                image_path = "https://raw.githubusercontent.com/Samuelchazy/Educative.io/19d3100db50749489689a5c21029c3499722b254/images/Toyota_4.jpg"
                st.image(image_path, use_column_width=True)

            with col_right:
                image_path = "https://raw.githubusercontent.com/Samuelchazy/Educative.io/19d3100db50749489689a5c21029c3499722b254/images/Toyota_5.jpg"
                st.image(image_path, use_column_width=True)

                image_path = "https://raw.githubusercontent.com/Samuelchazy/Educative.io/19d3100db50749489689a5c21029c3499722b254/images/Toyota_6.jpg"
                st.image(image_path, use_column_width=True)

        return content

    else:
        st.error('User Manuel not found')
        return None