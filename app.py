import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Kitty Housie Caller",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="collapsed",
)

html = r"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<style>
*{box-sizing:border-box}
html,body{
    margin:0;
    padding:0;
    background:#fff;
    color:#222;
    font-family:Arial,Helvetica,sans-serif;
    overflow:hidden
}
button{
    font-family:inherit;
    -webkit-tap-highlight-color:transparent
}

.app{
    width:100%;
    max-width:720px;
    min-height:100vh;
    margin:0 auto;
    padding:7px 9px 9px;
    position:relative;
    background:#fff;
}

/* TOP BAR */
.topbar{
    height:43px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    margin-bottom:4px;
}
.icon-btn{
    border:0;
    background:transparent;
    width:42px;
    height:42px;
    border-radius:10px;
    font-size:25px;
    cursor:pointer;
    display:flex;
    align-items:center;
    justify-content:center;
}
.menu-btn{font-size:27px}

.history-top{
    border:1px solid #d79d58;
    background:#fff9ef;
    color:#d78322;
    border-radius:8px;
    font-size:12px;
    font-weight:700;
    line-height:1.05;
    padding:6px 9px;
    height:40px;
}

.brand{
    font-size:19px;
    font-weight:800;
    color:#333;
}

/* CURRENT NUMBER */
.current-area{text-align:center}

.previous{
    height:24px;
    font-size:13px;
    color:#777;
    display:flex;
    justify-content:center;
    align-items:center;
    gap:6px;
}

.prev-value{
    font-weight:700;
    color:#555;
}

.current-number{
    height:94px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:82px;
    line-height:1;
    font-weight:800;
    color:#222;
}

.current-name{
    height:27px;
    font-size:17px;
    color:#555;
    font-weight:600;
}

/* SPEAKER */
.speaker-row{
    height:45px;
    display:flex;
    align-items:center;
    justify-content:flex-start;
    padding-left:3px;
}

.speaker{
    width:43px;
    height:43px;
    border-radius:50%;
    border:3px solid #8dcc8d;
    background:#fff;
    font-size:23px;
    cursor:pointer;
}

/* NEXT */
.next-row{
    height:75px;
    display:flex;
    align-items:center;
    justify-content:center;
}

.next{
    width:min(400px,78%);
    height:62px;
    border-radius:14px;
    border:1px solid #9c0000;
    background:linear-gradient(#f22b2b,#d90000);
    color:white;
    font-size:32px;
    font-weight:800;
    letter-spacing:.3px;
    box-shadow:0 3px 5px rgba(0,0,0,.25);
    cursor:pointer;
}

.next:active{
    transform:scale(.98);
}

/* GRID */
.number-grid{
    display:grid;
    grid-template-columns:repeat(10,1fr);
    gap:3px;
    width:100%;
}

.number{
    aspect-ratio:1/1;
    min-width:0;
    padding:0;
    border:3px solid #16b6d8;
    border-radius:0;
    background:#fff;
    color:#333;
    font-size:clamp(15px,4.7vw,28px);
    font-weight:400;
    cursor:pointer;
}

.number.called{
    background:#16b6d8;
    color:#fff;
}

.number.last{
    background:#f31d1d;
    color:#fff;
    border-color:#f31d1d;
    font-weight:800;
}

.number.called.last{
    background:#f31d1d;
    color:#fff;
}

/* STATUS */
.status{
    text-align:center;
    height:21px;
    line-height:21px;
    font-size:12px;
    color:#777;
}

/* DRAWER */
.overlay{
    position:fixed;
    inset:0;
    background:rgba(0,0,0,.38);
    display:none;
    z-index:20;
}

.overlay.show{
    display:block;
}

.drawer{
    position:absolute;
    top:0;
    left:0;
    width:min(310px,86vw);
    height:100%;
    background:#fff;
    box-shadow:5px 0 18px rgba(0,0,0,.22);
    padding:14px 16px;
    overflow-y:auto;
}

.drawer-head{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding-bottom:12px;
    border-bottom:1px solid #ddd;
    margin-bottom:10px;
}

.drawer-title{
    font-size:20px;
    font-weight:800;
}

.close{
    border:0;
    background:#eee;
    border-radius:50%;
    width:34px;
    height:34px;
    font-size:20px;
}

.menu-section{
    padding:12px 0;
    border-bottom:1px solid #eee;
}

.section-title{
    font-size:15px;
    font-weight:800;
    margin-bottom:9px;
}

.menu-action{
    width:100%;
    border:1px solid #ddd;
    background:#f8f8f8;
    border-radius:10px;
    padding:11px;
    text-align:left;
    font-size:15px;
    font-weight:700;
    margin:5px 0;
}

.menu-action.danger{
    color:#c62828;
    background:#fff2f2;
}

/* HISTORY MODAL */
.modal-wrap{
    position:fixed;
    inset:0;
    background:rgba(0,0,0,.42);
    display:none;
    align-items:center;
    justify-content:center;
    z-index:30;
    padding:18px;
}

.modal-wrap.show{
    display:flex;
}

.modal{
    width:min(430px,94vw);
    max-height:80vh;
    overflow:auto;
    background:#fff;
    border-radius:16px;
    padding:17px;
    box-shadow:0 8px 30px rgba(0,0,0,.3);
}

.modal-head{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:10px;
}

.modal-title{
    font-size:20px;
    font-weight:800;
}

.history-list{
    display:grid;
    grid-template-columns:repeat(5,1fr);
    gap:7px;
}

.history-item{
    border:2px solid #16b6d8;
    border-radius:8px;
    text-align:center;
    padding:8px 3px;
    font-size:17px;
    font-weight:700;
}

.empty{
    color:#888;
    text-align:center;
    padding:20px;
}

/* VERY SMALL PHONES */
@media(max-width:380px){
    .app{
        padding:4px 6px
    }

    .topbar{
        height:39px
    }

    .icon-btn{
        height:38px;
        width:38px
    }

    .brand{
        font-size:17px
    }

    .current-number{
        height:82px;
        font-size:72px
    }

    .next-row{
        height:68px
    }

    .next{
        height:57px;
        font-size:30px
    }

    .speaker-row{
        height:39px
    }

    .speaker{
        width:39px;
        height:39px
    }

    .number{
        border-width:2px;
        font-size:14px
    }

    .number-grid{
        gap:2px
    }
}
</style>
</head>

<body>

<div class="app">

    <div class="topbar">
        <button class="icon-btn menu-btn" id="menuButton" aria-label="Menu">☰</button>

        <div class="brand">🎉 Kitty Housie</div>

        <button class="history-top" id="historyButton">
            Number<br>History
        </button>
    </div>

    <div class="current-area">

        <div class="previous">
            <span>Prev. number:</span>
            <span class="prev-value" id="prevNumber">--</span>
        </div>

        <div class="current-number" id="currentNumber">--</div>

        <div class="current-name" id="currentName">
            Press NEXT to start
        </div>

    </div>

    <div class="speaker-row">
        <button class="speaker" id="speakerButton" aria-label="Speak">
            🔊
        </button>
    </div>

    <div class="next-row">
        <button class="next" id="nextButton">
            NEXT
        </button>
    </div>

    <div class="status" id="status">
        90 numbers remaining
    </div>

    <div class="number-grid" id="numberGrid"></div>

</div>


<!-- HAMBURGER DRAWER -->

<div class="overlay" id="menuOverlay">

    <div class="drawer" onclick="event.stopPropagation()">

        <div class="drawer-head">

            <div class="drawer-title">
                ☰ Game Settings
            </div>

            <button class="close" id="closeMenu">
                ×
            </button>

        </div>


        <div class="menu-section">

            <button class="menu-action" id="menuHistory">
                📜 Number History
            </button>

            <button class="menu-action" id="menuUndo">
                ↩️ Undo Last Number
            </button>

            <button class="menu-action danger" id="menuReset">
                🔄 New Game
            </button>

        </div>


        <div class="menu-section">

            <div style="font-size:12px;color:#888;text-align:center">
                Kitty Housie Caller<br>
                1–90 Tambola
            </div>

        </div>

    </div>

</div>


<!-- HISTORY -->

<div class="modal-wrap" id="historyModal">

    <div class="modal">

        <div class="modal-head">

            <div class="modal-title">
                📜 Number History
            </div>

            <button class="close" id="closeHistory">
                ×
            </button>

        </div>

        <div id="historyList" class="history-list"></div>

    </div>

</div>


<script>

const numbers = Array.from(
    {length:90},
    (_,i)=>i+1
);


const englishNumbers = {
1:"One",
2:"Two",
3:"Three",
4:"Four",
5:"Five",
6:"Six",
7:"Seven",
8:"Eight",
9:"Nine",
10:"Ten",
11:"Eleven",
12:"Twelve",
13:"Thirteen",
14:"Fourteen",
15:"Fifteen",
16:"Sixteen",
17:"Seventeen",
18:"Eighteen",
19:"Nineteen",
20:"Twenty",
21:"Twenty-one",
22:"Twenty-two",
23:"Twenty-three",
24:"Twenty-four",
25:"Twenty-five",
26:"Twenty-six",
27:"Twenty-seven",
28:"Twenty-eight",
29:"Twenty-nine",
30:"Thirty",
31:"Thirty-one",
32:"Thirty-two",
33:"Thirty-three",
34:"Thirty-four",
35:"Thirty-five",
36:"Thirty-six",
37:"Thirty-seven",
38:"Thirty-eight",
39:"Thirty-nine",
40:"Forty",
41:"Forty-one",
42:"Forty-two",
43:"Forty-three",
44:"Forty-four",
45:"Forty-five",
46:"Forty-six",
47:"Forty-seven",
48:"Forty-eight",
49:"Forty-nine",
50:"Fifty",
51:"Fifty-one",
52:"Fifty-two",
53:"Fifty-three",
54:"Fifty-four",
55:"Fifty-five",
56:"Fifty-six",
57:"Fifty-seven",
58:"Fifty-eight",
59:"Fifty-nine",
60:"Sixty",
61:"Sixty-one",
62:"Sixty-two",
63:"Sixty-three",
64:"Sixty-four",
65:"Sixty-five",
66:"Sixty-six",
67:"Sixty-seven",
68:"Sixty-eight",
69:"Sixty-nine",
70:"Seventy",
71:"Seventy-one",
72:"Seventy-two",
73:"Seventy-three",
74:"Seventy-four",
75:"Seventy-five",
76:"Seventy-six",
77:"Seventy-seven",
78:"Seventy-eight",
79:"Seventy-nine",
80:"Eighty",
81:"Eighty-one",
82:"Eighty-two",
83:"Eighty-three",
84:"Eighty-four",
85:"Eighty-five",
86:"Eighty-six",
87:"Eighty-seven",
88:"Eighty-eight",
89:"Eighty-nine",
90:"Ninety"
};


let calledNumbers = [];
let currentNumber = null;
let voiceType = "female";
let speedLevel = 4;
let speechGeneration = 0;


const grid = document.getElementById("numberGrid");


/* CREATE 1-90 GRID */

numbers.forEach(num => {

    const button = document.createElement("button");

    button.className = "number";

    button.textContent = num;

    button.dataset.number = num;

    button.addEventListener(
        "click",
        () => callNumber(num)
    );

    grid.appendChild(button);

});


/* SPEECH SPEED */

function getRate(){

    return {
        3:0.72,
        4:0.82,
        5:0.92,
        6:1.03,
        7:1.14
    }[speedLevel];

}


/* SPEAK */

function speak(text, generation){

    if(!window.speechSynthesis) return;

    const utterance =
        new SpeechSynthesisUtterance(text);

    utterance.lang = "en-IN";

    utterance.rate = getRate();

    utterance.pitch =
        voiceType === "female"
        ? 1.08
        : 0.82;

    utterance.volume = 1;


    const voices =
        window.speechSynthesis.getVoices();

    let selected =
        voices.find(
            v =>
            v.lang &&
            v.lang.toLowerCase()
            .startsWith("en-in")
        )
        ||
        voices.find(
            v =>
            v.lang &&
            v.lang.toLowerCase()
            .startsWith("en")
        );


    if(selected){
        utterance.voice = selected;
    }


    utterance.onend = () => {

        if(generation !== speechGeneration){
            return;
        }

    };


    window.speechSynthesis.speak(
        utterance
    );

}


/* ANNOUNCE NUMBER */

function announce(num){

    speechGeneration++;

    const generation =
        speechGeneration;

    window.speechSynthesis.cancel();


    /*
       Example:

       43

       First:
       Four

       Then:
       Three

       Then:
       Forty Three
    */

    const digits =
        String(num)
        .split("")
        .map(
            digit =>
            englishNumbers[
                Number(digit)
            ]
        );


    const fullNumber =
        englishNumbers[num];


    let sequence = [];


    digits.forEach(word => {

        sequence.push(word);

    });


    sequence.push(fullNumber);


    let delay = 0;


    sequence.forEach((word,index) => {

        setTimeout(() => {

            if(generation !== speechGeneration){
                return;
            }

            if(currentNumber !== num){
                return;
            }

            speak(
                word,
                generation
            );

        }, delay);


        delay += 850;

    });

}


/* CALL NUMBER */

function callNumber(num){

    /*
       If already called:
       Do not add it again.
       Simply announce it again.
    */

    if(calledNumbers.includes(num)){

        currentNumber = num;

        updateDisplay();

        announce(num);

        return;

    }


    calledNumbers.push(num);

    currentNumber = num;

    updateDisplay();

    announce(num);

}


/* NEXT RANDOM NUMBER */

function nextNumber(){

    const remaining =
        numbers.filter(
            n => !calledNumbers.includes(n)
        );


    if(!remaining.length){

        alert(
            "All 90 numbers have been called!"
        );

        return;

    }


    const randomIndex =
        Math.floor(
            Math.random() *
            remaining.length
        );


    const randomNumber =
        remaining[randomIndex];


    callNumber(randomNumber);

}


/* UPDATE DISPLAY */

function updateDisplay(){

    document.getElementById(
        "currentNumber"
    ).textContent =
        currentNumber === null
        ? "--"
        : currentNumber;


    document.getElementById(
        "currentName"
    ).textContent =
        currentNumber === null
        ? "Press NEXT to start"
        : englishNumbers[currentNumber];


    const prev =
        calledNumbers.length >= 2
        ? calledNumbers[
            calledNumbers.length - 2
        ]
        : "--";


    document.getElementById(
        "prevNumber"
    ).textContent = prev;


    document.getElementById(
        "status"
    ).textContent =
        (90 - calledNumbers.length)
        + " numbers remaining";


    document
        .querySelectorAll(".number")
        .forEach(button => {

            const n =
                Number(button.dataset.number);

            button.classList.remove(
                "called",
                "last"
            );


            if(
                calledNumbers.includes(n)
            ){
                button.classList.add(
                    "called"
                );
            }


            if(n === currentNumber){

                button.classList.add(
                    "last"
                );

            }

        });

}


/* UNDO */

function undo(){

    if(!calledNumbers.length){
        return;
    }


    calledNumbers.pop();


    currentNumber =
        calledNumbers.length
        ? calledNumbers[
            calledNumbers.length - 1
        ]
        : null;


    speechGeneration++;

    window.speechSynthesis.cancel();


    updateDisplay();

}


/* RESET */

function resetGame(){

    if(
        !confirm(
            "Start a new Housie game?"
        )
    ){
        return;
    }


    calledNumbers = [];

    currentNumber = null;

    speechGeneration++;

    window.speechSynthesis.cancel();

    updateDisplay();

}


/* HISTORY */

function showHistory(){

    const list =
        document.getElementById(
            "historyList"
        );


    list.innerHTML = "";


    if(!calledNumbers.length){

        list.innerHTML =
            '<div class="empty" style="grid-column:1/-1">No numbers called yet.</div>';

    }
    else{

        [
            ...calledNumbers
        ]
        .reverse()
        .forEach(
            (n,i) => {

                const item =
                    document.createElement(
                        "div"
                    );

                item.className =
                    "history-item";

                item.textContent = n;

                item.title =
                    (i === 0
                        ? "Latest"
                        : "")
                    + " "
                    + englishNumbers[n];

                list.appendChild(
                    item
                );

            }
        );

    }


    document
        .getElementById(
            "historyModal"
        )
        .classList.add("show");

}


/* MENU */

function openMenu(){

    document
        .getElementById(
            "menuOverlay"
        )
        .classList.add("show");

}


function closeMenu(){

    document
        .getElementById(
            "menuOverlay"
        )
        .classList.remove("show");

}


/* NEXT BUTTON */

document
    .getElementById("nextButton")
    .addEventListener(
        "click",
        nextNumber
    );


/* SPEAKER BUTTON */

document
    .getElementById("speakerButton")
    .addEventListener(
        "click",
        () => {

            if(
                currentNumber !== null
            ){

                announce(
                    currentNumber
                );

            }

        }
    );


/* MENU BUTTON */

document
    .getElementById("menuButton")
    .addEventListener(
        "click",
        openMenu
    );


document
    .getElementById("closeMenu")
    .addEventListener(
        "click",
        closeMenu
    );


document
    .getElementById("menuOverlay")
    .addEventListener(
        "click",
        closeMenu
    );


/* HISTORY */

document
    .getElementById("historyButton")
    .addEventListener(
        "click",
        showHistory
    );


document
    .getElementById("menuHistory")
    .addEventListener(
        "click",
        () => {

            closeMenu();

            showHistory();

        }
    );


/* UNDO */

document
    .getElementById("menuUndo")
    .addEventListener(
        "click",
        () => {

            undo();

            closeMenu();

        }
    );


/* RESET */

document
    .getElementById("menuReset")
    .addEventListener(
        "click",
        () => {

            resetGame();

            closeMenu();

        }
    );


/* CLOSE HISTORY */

document
    .getElementById("closeHistory")
    .addEventListener(
        "click",
        () => {

            document
                .getElementById(
                    "historyModal"
                )
                .classList.remove(
                    "show"
                );

        }
    );


document
    .getElementById("historyModal")
    .addEventListener(
        "click",
        e => {

            if(
                e.target.id ===
                "historyModal"
            ){

                document
                    .getElementById(
                        "historyModal"
                    )
                    .classList.remove(
                        "show"
                    );

            }

        }
    );


/* LOAD BROWSER VOICES */

if(window.speechSynthesis){

    window.speechSynthesis.onvoiceschanged =
        () =>
        window.speechSynthesis.getVoices();

}


/* INITIAL DISPLAY */

updateDisplay();

</script>

</body>
</html>
"""

components.html(
    html,
    height=900,
    scrolling=False
)
