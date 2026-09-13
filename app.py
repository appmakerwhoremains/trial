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
html,body{margin:0;padding:0;background:#fff;color:#222;font-family:Arial,Helvetica,sans-serif;overflow:hidden}
button{font-family:inherit;-webkit-tap-highlight-color:transparent}

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
.prev-value{font-weight:700;color:#555}

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
    width:43px;height:43px;
    border-radius:50%;
    border:3px solid #8dcc8d;
    background:#fff;
    font-size:23px;
    cursor:pointer;
}

/* PLAY */
.play-row{
    height:75px;
    display:flex;
    align-items:center;
    justify-content:center;
}
.play{
    width:min(400px,78%);
    height:62px;
    border-radius:14px;
    border:1px solid #9c0000;
    background:linear-gradient(#f22b2b,#d90000);
    color:white;
    font-size:39px;
    font-weight:800;
    letter-spacing:.3px;
    box-shadow:0 3px 5px rgba(0,0,0,.25);
    cursor:pointer;
}
.play:active{transform:scale(.98)}
.play.auto-active{background:linear-gradient(#ff5050,#c90000)}

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
.overlay.show{display:block}
.drawer{
    position:absolute;
    top:0;left:0;
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
.drawer-title{font-size:20px;font-weight:800}
.close{border:0;background:#eee;border-radius:50%;width:34px;height:34px;font-size:20px}
.menu-section{padding:12px 0;border-bottom:1px solid #eee}
.section-title{font-size:15px;font-weight:800;margin-bottom:9px}
.menu-row{
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:10px;
    margin:7px 0;
}
.small-buttons{display:flex;gap:6px;flex-wrap:wrap}
.option{
    border:1px solid #ccc;
    background:#fafafa;
    border-radius:9px;
    padding:8px 11px;
    font-size:14px;
    cursor:pointer;
}
.option.active{background:#16b6d8;color:#fff;border-color:#16b6d8}
.toggle{
    width:53px;height:29px;
    border-radius:18px;
    background:#aaa;
    border:0;
    padding:3px;
    cursor:pointer;
}
.toggle span{
    display:block;width:23px;height:23px;border-radius:50%;
    background:#fff;transition:.2s;
}
.toggle.on{background:#55ae55}
.toggle.on span{transform:translateX(24px)}
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
.menu-action.danger{color:#c62828;background:#fff2f2}

/* HISTORY MODAL */
.modal-wrap{
    position:fixed;inset:0;
    background:rgba(0,0,0,.42);
    display:none;
    align-items:center;
    justify-content:center;
    z-index:30;
    padding:18px;
}
.modal-wrap.show{display:flex}
.modal{
    width:min(430px,94vw);
    max-height:80vh;
    overflow:auto;
    background:#fff;
    border-radius:16px;
    padding:17px;
    box-shadow:0 8px 30px rgba(0,0,0,.3);
}
.modal-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px}
.modal-title{font-size:20px;font-weight:800}
.history-list{display:grid;grid-template-columns:repeat(5,1fr);gap:7px}
.history-item{
    border:2px solid #16b6d8;
    border-radius:8px;
    text-align:center;
    padding:8px 3px;
    font-size:17px;
    font-weight:700;
}
.empty{color:#888;text-align:center;padding:20px}

/* VERY SMALL PHONES */
@media(max-width:380px){
    .app{padding:4px 6px}
    .topbar{height:39px}
    .icon-btn{height:38px;width:38px}
    .brand{font-size:17px}
    .current-number{height:82px;font-size:72px}
    .play-row{height:68px}
    .play{height:57px;font-size:34px}
    .speaker-row{height:39px}
    .speaker{width:39px;height:39px}
    .number{border-width:2px;font-size:14px}
    .number-grid{gap:2px}
}
</style>
</head>

<body>
<div class="app">

    <div class="topbar">
        <button class="icon-btn menu-btn" id="menuButton" aria-label="Menu">☰</button>
        <div class="brand">🎉 Kitty Housie</div>
        <button class="history-top" id="historyButton">Number<br>History</button>
    </div>

    <div class="current-area">
        <div class="previous">
            <span>Prev. number:</span>
            <span class="prev-value" id="prevNumber">--</span>
        </div>

        <div class="current-number" id="currentNumber">--</div>
        <div class="current-name" id="currentName">Press PLAY to start</div>
    </div>

    <div class="speaker-row">
        <button class="speaker" id="speakerButton" aria-label="Speak">🔊</button>
    </div>

    <div class="play-row">
        <button class="play" id="playButton">Play</button>
    </div>

    <div class="status" id="status">90 numbers remaining</div>

    <div class="number-grid" id="numberGrid"></div>

</div>

<!-- HAMBURGER DRAWER -->
<div class="overlay" id="menuOverlay">
    <div class="drawer" onclick="event.stopPropagation()">
        <div class="drawer-head">
            <div class="drawer-title">☰ Game Settings</div>
            <button class="close" id="closeMenu">×</button>
        </div>

        <div class="menu-section">
            <div class="section-title">🤖 Auto Calling</div>
            <div class="menu-row">
                <span>Automatic next number</span>
                <button class="toggle" id="autoToggle"><span></span></button>
            </div>
        </div>

        <div class="menu-section">
            <div class="section-title">🎙️ Announcement Language</div>
            <div class="small-buttons">
                <button class="option active" data-lang="both">🔄 Both</button>
                <button class="option" data-lang="english">🇬🇧 English</button>
                <button class="option" data-lang="hindi">🇮🇳 हिंदी</button>
            </div>
        </div>

        <div class="menu-section">
            <div class="section-title">🔊 Voice</div>
            <div class="small-buttons">
                <button class="option active" data-voice="female">Female</button>
                <button class="option" data-voice="male">Male</button>
            </div>
        </div>

        <div class="menu-section">
            <div class="section-title">⚡ Announcement Speed</div>
            <div class="small-buttons">
                <button class="option" data-speed="3">3</button>
                <button class="option active" data-speed="4">4</button>
                <button class="option" data-speed="5">5</button>
                <button class="option" data-speed="6">6</button>
                <button class="option" data-speed="7">7</button>
            </div>
            <div style="font-size:12px;color:#777;margin-top:7px">
                Higher number = faster automatic calling.
            </div>
        </div>

        <div class="menu-section">
            <button class="menu-action" id="menuHistory">📜 Number History</button>
            <button class="menu-action" id="menuUndo">↩️ Undo Last Number</button>
            <button class="menu-action danger" id="menuReset">🔄 New Game</button>
        </div>

        <div class="menu-section">
            <div style="font-size:12px;color:#888;text-align:center">
                Kitty Housie Caller<br>1–90 Tambola
            </div>
        </div>
    </div>
</div>

<!-- HISTORY -->
<div class="modal-wrap" id="historyModal">
    <div class="modal">
        <div class="modal-head">
            <div class="modal-title">📜 Number History</div>
            <button class="close" id="closeHistory">×</button>
        </div>
        <div id="historyList" class="history-list"></div>
    </div>
</div>

<script>
const numbers = Array.from({length:90}, (_,i)=>i+1);

const englishNumbers = {
1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",
11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",
21:"Twenty-one",22:"Twenty-two",23:"Twenty-three",24:"Twenty-four",25:"Twenty-five",26:"Twenty-six",27:"Twenty-seven",28:"Twenty-eight",29:"Twenty-nine",30:"Thirty",
31:"Thirty-one",32:"Thirty-two",33:"Thirty-three",34:"Thirty-four",35:"Thirty-five",36:"Thirty-six",37:"Thirty-seven",38:"Thirty-eight",39:"Thirty-nine",40:"Forty",
41:"Forty-one",42:"Forty-two",43:"Forty-three",44:"Forty-four",45:"Forty-five",46:"Forty-six",47:"Forty-seven",48:"Forty-eight",49:"Forty-nine",50:"Fifty",
51:"Fifty-one",52:"Fifty-two",53:"Fifty-three",54:"Fifty-four",55:"Fifty-five",56:"Fifty-six",57:"Fifty-seven",58:"Fifty-eight",59:"Fifty-nine",60:"Sixty",
61:"Sixty-one",62:"Sixty-two",63:"Sixty-three",64:"Sixty-four",65:"Sixty-five",66:"Sixty-six",67:"Sixty-seven",68:"Sixty-eight",69:"Sixty-nine",70:"Seventy",
71:"Seventy-one",72:"Seventy-two",73:"Seventy-three",74:"Seventy-four",75:"Seventy-five",76:"Seventy-six",77:"Seventy-seven",78:"Seventy-eight",79:"Seventy-nine",80:"Eighty",
81:"Eighty-one",82:"Eighty-two",83:"Eighty-three",84:"Eighty-four",85:"Eighty-five",86:"Eighty-six",87:"Eighty-seven",88:"Eighty-eight",89:"Eighty-nine",90:"Ninety"
};

const hindiNumbers = {
1:"एक",2:"दो",3:"तीन",4:"चार",5:"पाँच",6:"छह",7:"सात",8:"आठ",9:"नौ",10:"दस",
11:"ग्यारह",12:"बारह",13:"तेरह",14:"चौदह",15:"पंद्रह",16:"सोलह",17:"सत्रह",18:"अठारह",19:"उन्नीस",20:"बीस",
21:"इक्कीस",22:"बाईस",23:"तेईस",24:"चौबीस",25:"पच्चीस",26:"छब्बीस",27:"सत्ताईस",28:"अट्ठाईस",29:"उनतीस",30:"तीस",
31:"इकतीस",32:"बत्तीस",33:"तैंतीस",34:"चौंतीस",35:"पैंतीस",36:"छत्तीस",37:"सैंतीस",38:"अड़तीस",39:"उनतालीस",40:"चालीस",
41:"इकतालीस",42:"बयालीस",43:"तैंतालीस",44:"चवालीस",45:"पैंतालीस",46:"छियालीस",47:"सैंतालीस",48:"अड़तालीस",49:"उनचास",50:"पचास",
51:"इक्यावन",52:"बावन",53:"तिरेपन",54:"चौवन",55:"पचपन",56:"छप्पन",57:"सत्तावन",58:"अट्ठावन",59:"उनसठ",60:"साठ",
61:"इकसठ",62:"बासठ",63:"तिरसठ",64:"चौंसठ",65:"पैंसठ",66:"छियासठ",67:"सड़सठ",68:"अड़सठ",69:"उनहत्तर",70:"सत्तर",
71:"इकहत्तर",72:"बहत्तर",73:"तिहत्तर",74:"चौहत्तर",75:"पचहत्तर",76:"छिहत्तर",77:"सतहत्तर",78:"अठहत्तर",79:"उन्नासी",80:"अस्सी",
81:"इक्यासी",82:"बयासी",83:"तिरासी",84:"चौरासी",85:"पचासी",86:"छियासी",87:"सत्तासी",88:"अट्ठासी",89:"नवासी",90:"नब्बे"
};

let calledNumbers = [];
let currentNumber = null;
let language = "both";
let voiceType = "female";
let speedLevel = 4;
let autoCalling = false;
let autoTimer = null;
let speechGeneration = 0;

const grid = document.getElementById("numberGrid");

numbers.forEach(num => {
    const button = document.createElement("button");
    button.className = "number";
    button.textContent = num;
    button.dataset.number = num;
    button.addEventListener("click", () => callNumber(num));
    grid.appendChild(button);
});

function getRate(){
    return {3:0.72,4:0.82,5:0.92,6:1.03,7:1.14}[speedLevel];
}

function speak(text, lang, generation){
    if (!window.speechSynthesis) return;

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = lang;
    utterance.rate = getRate();
    utterance.pitch = voiceType === "female" ? 1.08 : 0.82;
    utterance.volume = 1;

    const voices = window.speechSynthesis.getVoices();
    let selected = null;

    if(lang === "hi-IN"){
        selected = voices.find(v => v.lang && v.lang.toLowerCase().startsWith("hi"));
    }else{
        selected = voices.find(v => v.lang && v.lang.toLowerCase().startsWith("en-in"))
                || voices.find(v => v.lang && v.lang.toLowerCase().startsWith("en"));
    }

    if(selected) utterance.voice = selected;

    utterance.onend = () => {
        if(generation !== speechGeneration) return;
    };

    window.speechSynthesis.speak(utterance);
}

function announce(num){
    speechGeneration++;
    const generation = speechGeneration;
    window.speechSynthesis.cancel();

    const en = englishNumbers[num];
    const hi = hindiNumbers[num];

    if(language === "english"){
        speak(en, "en-IN", generation);
    }else if(language === "hindi"){
        speak(hi, "hi-IN", generation);
    }else{
        speak(en, "en-IN", generation);
        setTimeout(() => {
            if(generation === speechGeneration && currentNumber === num){
                speak(hi, "hi-IN", generation);
            }
        }, 1000);
    }
}

function callNumber(num){
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

    if(autoCalling){
        scheduleAuto();
    }
}

function updateDisplay(){
    document.getElementById("currentNumber").textContent =
        currentNumber === null ? "--" : currentNumber;

    document.getElementById("currentName").textContent =
        currentNumber === null
        ? "Press PLAY to start"
        : englishNumbers[currentNumber] + " • " + hindiNumbers[currentNumber];

    const prev = calledNumbers.length >= 2
        ? calledNumbers[calledNumbers.length-2]
        : "--";
    document.getElementById("prevNumber").textContent = prev;

    document.getElementById("status").textContent =
        (90 - calledNumbers.length) + " numbers remaining";

    document.querySelectorAll(".number").forEach(button => {
        const n = Number(button.dataset.number);
        button.classList.remove("called","last");

        if(calledNumbers.includes(n)) button.classList.add("called");
        if(n === currentNumber) button.classList.add("last");
    });
}

function randomNext(){
    const remaining = numbers.filter(n => !calledNumbers.includes(n));

    if(!remaining.length){
        stopAuto();
        alert("All 90 numbers have been called!");
        return;
    }

    const n = remaining[Math.floor(Math.random()*remaining.length)];
    callNumber(n);
}

function scheduleAuto(){
    clearTimeout(autoTimer);
    if(!autoCalling) return;

    // Speed 3 = slower, Speed 7 = faster.
    const delays = {3:7000,4:6000,5:5000,6:4000,7:3000};
    autoTimer = setTimeout(() => {
        if(autoCalling) randomNext();
    }, delays[speedLevel]);
}

function startAuto(){
    autoCalling = true;
    document.getElementById("autoToggle").classList.add("on");
    document.getElementById("playButton").classList.add("auto-active");
    document.getElementById("playButton").textContent = "Pause";
    randomNext();
}

function stopAuto(){
    autoCalling = false;
    clearTimeout(autoTimer);
    document.getElementById("autoToggle").classList.remove("on");
    document.getElementById("playButton").classList.remove("auto-active");
    document.getElementById("playButton").textContent = "Play";
}

function toggleAuto(){
    if(autoCalling) stopAuto();
    else startAuto();
}

function undo(){
    stopAuto();
    if(!calledNumbers.length) return;

    calledNumbers.pop();
    currentNumber = calledNumbers.length
        ? calledNumbers[calledNumbers.length-1]
        : null;

    speechGeneration++;
    window.speechSynthesis.cancel();
    updateDisplay();
}

function resetGame(){
    stopAuto();
    if(!confirm("Start a new Housie game?")) return;

    calledNumbers = [];
    currentNumber = null;
    speechGeneration++;
    window.speechSynthesis.cancel();
    updateDisplay();
}

function showHistory(){
    const list = document.getElementById("historyList");
    list.innerHTML = "";

    if(!calledNumbers.length){
        list.innerHTML = '<div class="empty" style="grid-column:1/-1">No numbers called yet.</div>';
    }else{
        [...calledNumbers].reverse().forEach((n,i) => {
            const item = document.createElement("div");
            item.className = "history-item";
            item.textContent = n;
            item.title = (i === 0 ? "Latest" : "") + " " + englishNumbers[n];
            list.appendChild(item);
        });
    }

    document.getElementById("historyModal").classList.add("show");
}

function openMenu(){
    document.getElementById("menuOverlay").classList.add("show");
}
function closeMenu(){
    document.getElementById("menuOverlay").classList.remove("show");
}

/* Main controls */
document.getElementById("playButton").addEventListener("click", toggleAuto);
document.getElementById("speakerButton").addEventListener("click", () => {
    if(currentNumber !== null) announce(currentNumber);
});

/* Menu */
document.getElementById("menuButton").addEventListener("click", openMenu);
document.getElementById("closeMenu").addEventListener("click", closeMenu);
document.getElementById("menuOverlay").addEventListener("click", closeMenu);

document.getElementById("autoToggle").addEventListener("click", toggleAuto);

document.querySelectorAll("[data-lang]").forEach(btn => {
    btn.addEventListener("click", () => {
        language = btn.dataset.lang;
        document.querySelectorAll("[data-lang]").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
    });
});

document.querySelectorAll("[data-voice]").forEach(btn => {
    btn.addEventListener("click", () => {
        voiceType = btn.dataset.voice;
        document.querySelectorAll("[data-voice]").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
    });
});

document.querySelectorAll("[data-speed]").forEach(btn => {
    btn.addEventListener("click", () => {
        speedLevel = Number(btn.dataset.speed);
        document.querySelectorAll("[data-speed]").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        if(autoCalling) scheduleAuto();
    });
});

document.getElementById("historyButton").addEventListener("click", showHistory);
document.getElementById("menuHistory").addEventListener("click", () => {
    closeMenu();
    showHistory();
});
document.getElementById("menuUndo").addEventListener("click", () => {
    undo();
    closeMenu();
});
document.getElementById("menuReset").addEventListener("click", () => {
    resetGame();
    closeMenu();
});

document.getElementById("closeHistory").addEventListener("click", () => {
    document.getElementById("historyModal").classList.remove("show");
});
document.getElementById("historyModal").addEventListener("click", e => {
    if(e.target.id === "historyModal"){
        document.getElementById("historyModal").classList.remove("show");
    }
});

/* Load voices where browsers provide them asynchronously */
if(window.speechSynthesis){
    window.speechSynthesis.onvoiceschanged = () => window.speechSynthesis.getVoices();
}

updateDisplay();
</script>
</body>
</html>
"""

components.html(html, height=900, scrolling=False)
