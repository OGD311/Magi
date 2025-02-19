## Magi
A *very simplistic* recreation of the Magi supercomputer system from Neon Genesis Evangelion using Ollama.<br>
The system is comprised of the Three Magi - Balthasar, Melchior and Casper; whom all inherit different traits from their creator Naoko Akagi's personality.<br>
As well as these different personalities, I also chose to use three different LLMs to add some more variation: mistral:7b, llama3.2:3b and zephyr:7b.

# Getting started
Requirements:
- Ollama
- Python

First clone this repository ```git clone https://github.com/OGD311/Magi.git ```<br>
Secondly ensure you have the ollama python package installed - ```pip install ollama```<br>
Finally run ```python .\magi.app.py ``` and navigate to localhost:8080<br>
> These LLMs do need to be installed BEFORE the python script is ran - their total size is approximately 12gb

# Outcomes
There are several states the responses can be categorised as, these are:
- Yes (Solid green)
- No (Solid red)
- Conditional (Striped green)
- Unclear (Striped red and green)

In the cases where it is not clear about an outcome, clicking on the Magi will reveal a popup with the LLMs exact response and how it has come to that conclusion

# Gallery
![image](https://github.com/user-attachments/assets/eb19c19f-00e0-47d7-b511-90818fb88732)
![image](https://github.com/user-attachments/assets/4d968a49-35db-4d1d-9e1f-5648e0fcbfc2)
![image](https://github.com/user-attachments/assets/3c6bbd60-ca6e-4668-b63a-8cf8d43ff7c1)
