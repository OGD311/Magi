
function pose(question) {
    
    if (!question) {
        console.error('Question is required');
        return;
    }

    const endpoints = {
        casper: '/casper',
        melchior: '/melchior',
        balthasar: '/balthasar'
    };

    function updateBotResponse(bot, question) {
        const botDiv = document.getElementById(bot);
        botDiv.classList.remove('yes', 'no', 'conditional');
        botDiv.classList.add('thinking');

        const delay = ((Math.random() * 100) + 100).toFixed(0) + 'ms';

        botDiv.style.setProperty('--animation-delay', delay);


        fetch(endpoints[bot], {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question })
        })
        .then(response => response.json())
        .then(data => {
            const botDiv = document.getElementById(bot);
            
            if (botDiv) {
                const answerClass = data[`${bot}_answer`] ;
                const explanation = data[`${bot}_full`] ;

                botDiv.classList.remove('yes', 'no', 'conditional', 'thinking');
                botDiv.classList.add(answerClass);

                botDiv.dataset.explanation = explanation;
            } else {
                console.error(`${bot} div not found`);
            }
        })
        .catch(error => console.error('Error:', error));
    }

    updateBotResponse('casper', question);
    updateBotResponse('melchior', question);
    updateBotResponse('balthasar', question);
}

function toggleExplanation(event) {
    const botDiv = event.currentTarget;
    let explanationText = botDiv.querySelector('.explanation');

    document.querySelectorAll('#magi > div > .explanation').forEach(element => {
        element.style.display = 'none'
    });

    if (!explanationText) {
        explanationText = document.createElement('p');
        explanationText.classList.add('explanation');
        explanationText.textContent = botDiv.dataset.explanation || "No explanation available";
        botDiv.appendChild(explanationText);
        explanationText.style.display = 'block';

        explanationText.onclick = function() {
            explanationText.style.display = 'none';
        };
    } else {
        explanationText.style.display = explanationText.style.display === 'none' ? 'block' : 'none';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    ['casper', 'melchior', 'balthasar'].forEach(bot => {
        const botDiv = document.getElementById(bot);
        if (botDiv) {
            botDiv.addEventListener('click', toggleExplanation);
        }
    });
});

document.getElementById('questionForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const question = document.getElementById('questionInput').value; 
    pose(question); 
});
