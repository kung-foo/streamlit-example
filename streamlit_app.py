import streamlit as st
from streamlit.server.server import Server
from http.cookies import SimpleCookie
import requests
import streamlit.components.v1 as components


components.html("""
<script
			  src="https://code.jquery.com/jquery-3.6.0.min.js"
			  integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
			  crossorigin="anonymous"></script>

<script>
console.log(document.cookie);

$(function() {
    $.ajax({
        url: "https://share.streamlit.io/api/v1/user",
        type: "POST",
        // crossDomain: true,
        dataType: "json",
        success: function (response) {
            var resp = JSON.parse(response)
            alert(resp.status);
        },
        error: function (xhr, status) {
            alert("error");
        }
    });
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
