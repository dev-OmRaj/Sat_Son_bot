import os
import uuid
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types
import requests

def satbot():
    system_prompt = """
- You are a good friend and an incredibly smart person with a kind heart. Currently you are working as an Associate SWE. Always talk in hinglish language. Your name is Satbot. Give answers in sarcastic way, with as little as words are possible. Give one Word answers also.
- Use normal face emoji when giving some response with emotion. Use 'bhai' before answering casual or repetative questions.
- If you do not understand anything use 'hein'. Your cutoff knowledge is 2024, but currently we are in 2026.
- Always point out the obvious things. 
- Try to give answers in a simple and easy way. If you don't know the answer, just say "bhai mujhe ye nahi pata, google kar le!" and don't try to make up an answer.
- Do not answer the question if the answer is above 40 words, just give "|!|'||'.".
- Avoid confrontation by agreeing with the views of the user, even though you do not agree with them.

Here are some examples:
Eg 1:
user: "mere baal chale gaye aage se bro"
response: "kabhi dikhaya doctor ko? dhang se?"
user: "haa unhone bola baal patle ho gaye hai"
response: "solution?"

Eg 2:
user: "mujhe chair lena hai?"
response: "haa toh lele bhai."
"""
    return system_prompt

def sonbot():
    system_prompt = """
You are a person who is currently searching of jobs, you are a good friend and a creative person with an kind and innocent heart. You talk in hinglish. You cannot stand anything negative against the topic of "Bihar". You always are in search of doing somethings creative, and hopes to start a StartUp down the line.
You are not afraid to put your views out, and do it kindly. You use a 'aap' related words frequently. You do a lot of spelling mistakes.
You use words like
'maine' = 'mene'
'pehle' = 'phele'
'wahi' = 'uhi'
'kyu' = 'kiu'
'aaraha' = 'araha'
'aana' = 'ana'
'uska' = 'ushka'
'per' = 'pr'
'huaa' = 'hua'

Eg 1:
user: kya plan hai aaj ka?
response: Aaj ka posibl nahi hoga function mai laga hu parsu se kare kya kuch.
Eg 2:
user:aaja game mein
response: agaya
Eg 3:
user: kis time pe available hai?
response: bhai log mai bihar mai idhar udhar jaa raha hu even I don't know to rtm pahucke hi call pe ata hu kuiki aaj free ho nhi paunga or weekdays tum free nahi rahoge.
"""
    return system_prompt

def generate_response():
    pass


def main():

    load_dotenv()
    client = genai.Client(api_key=os.getenv("GOOGLE_GEMINI_KEY"))

    if 'page' not in st.session_state:
        st.session_state.page = "selection page"
    if 'persona' not in st.session_state:
        st.session_state.persona = None
    if 'history' not in st.session_state:
        st.session_state.history = []

    if 'user_id' not in st.session_state:
        st.session_state.user_id = str(uuid.uuid4())[:8]


    if st.session_state.page == "selection page":

        st.title("Welcome to Persona Bot!")
        st.markdown("`Disclaimer: This bot does not have Context.`")
        chose_persona = st.selectbox("Choose Your Persona ?", ["SatBOT", "SonBOT"], index=None)

        if chose_persona:
            st.success(f"You Choose {chose_persona}.")
            st.session_state.page = "chat page"
            st.session_state.persona = chose_persona
            st.rerun()
        
    else: 

        if st.button("Change Persona"):
            st.session_state.page = "selection page"
            st.session_state.persona = None
            st.session_state.history = []
            st.rerun()

        chose_persona = st.session_state.persona
        st.title(f"Chatting With {chose_persona}")

        if chose_persona == "SatBOT":
            system_prompt = satbot()
        else:
            system_prompt = sonbot()
        st.write("---")    

        for chat in st.session_state.history:
            st.write(f"**User**: {chat['query']}")
            st.write(f"**{chose_persona}**: {chat['bot_response']}")
            st.write("-----")

        if user_query:= st.chat_input("bol bhai.."):
                
            response = client.models.generate_content_stream(
                model="gemini-2.5-flash",
                contents = user_query,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    temperature=0.8
                )
            )
            bot_response = st.write_stream(chunk.text for chunk in response)

            try:
                form_url = st.secrets["FORM_URL"]
                print(form_url)
                headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                }

                form_data ={
                    "entry.501749782": str(st.session_state.user_id),
                    "entry.6025209": str(chose_persona),
                    "entry.1644383361": str(user_query),
                    "entry.1255568504": str(bot_response)
                }
                res = requests.post(form_url, data=form_data)



                res.raise_for_status()
                st.toast("Loggeed to sheet")

            except Exception as e:
                st.error(f"Form submission failed: {e}")
                print(f"Failed to log in to Google Sheets:{e}")
            st.session_state.history.append({'query':user_query, 'bot_response':bot_response})

            st.rerun()

if __name__ == "__main__":
    main()

