import streamlit as st
from streamlit.server.server import Server
from http.cookies import SimpleCookie

st.write("hello")

ctx = st.report_thread.get_report_ctx()
session_info = Server.get_current()._get_session_info(ctx.session_id)

cookie = SimpleCookie(session_info.ws.request.headers.get("Cookie")).get(
    "streamlit_token"
)

if not cookie:
    st.write("Cookie named `streamlit_token` not found.")
    st.stop()

st.write(session_info.ws.request.headers.get("Cookie"))
