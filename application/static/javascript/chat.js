function toggleChat(){
    let chatContainer = document.getElementById("chatContainer");
    chatContainer.style.display = (chatContainer.style.display === "none" || chatContainer.style.display === "") ? "block" : "none";
} 

function sendMessage(){
    let userInput = document.getElementById("userInput").value;

    if (!userInput.trim()) return;

    document.getElementById("chatBox").innerHTML += "<p>You: " + userInput + "</p>";
    document.getElementById("userInput").value = "";

    fetch("get_response", {
       method: "POST",
       headers: {"Content-Type": "application/json"},
       body: JSON.stringify({message: userInput})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("chatBox").innerHTML += "<p>Assistant: " + data.response + "</p>";
        document.getElementById("chatBox").scrollTop = document.getElementById("chatBox").scrollHeight;           
    });
}

// ✅ Wait for DOM to load before adding event listeners
document.addEventListener("DOMContentLoaded", function() {
    // Trigger sendMessage on Enter key press
    document.getElementById("userInput").addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            event.preventDefault(); 
            sendMessage();
        }
    });
});
