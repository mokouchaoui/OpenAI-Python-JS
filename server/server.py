# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    server.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mokoucha <mokoucha@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/08 14:48:55 by mokoucha          #+#    #+#              #
#    Updated: 2023/01/08 14:48:57 by mokoucha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import openai
from flask import Flask, request
from flask_cors import cross_origin

app = Flask(__name__)

@app.route("/ask", methods=["GET"])
@cross_origin()
def ask():
    openai.api_key = "[YOUR_API_KEY_HERE]"
    
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=request.args['q'],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    message = completions.choices[0].text
    return {"answers": message}
    
if __name__ == "__main__":
    app.run(debug=True)