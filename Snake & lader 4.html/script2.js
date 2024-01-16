document.addEventListener('keydown',async(e)=>{
    if(e.keyCode=='81' && !stopEvent){
        stopEvent = true
        let dicNum = await roll()
        let isOutOfRange =checkRange(dicNum)
        await new Promise(resolve => setTimeout(resolve,400))
        if(!isOutOfRange){
        await run(dicNum)
        await new Promise(resolve => setTimeout(resolve,400))
        }
        let WonBy = checkWin()
        if(WonBy=='none'){
        
        changeTurn()
        stopEvent = false
        }
    }
})

let playerPositions = [0, 0];
let currentPlayer = 0;

function rollDie() {
  return Math.floor(Math.random() * 6) + 1;
}

function movePlayer(playerIndex, roll) {
  playerPositions[playerIndex] += roll;
  console.log(`Player ${playerIndex + 1} rolled a ${roll} and moved to position ${playerPositions[playerIndex]}`);
  
  const snakesAndLadders = {

  };
  
  
  if (snakesAndLadders[playerPositions[playerIndex]]) {
    const newPosition = snakesAndLadders[playerPositions[playerIndex]];
    if (newPosition > playerPositions[playerIndex]) {
      console.log(`Player ${playerIndex + 1} climbed a ladder and moved to position ${newPosition}`);
    } else {
      console.log(`Player ${playerIndex + 1} encountered a snake and moved to position ${newPosition}`);
    }
    playerPositions[playerIndex] = newPosition;
  }
}

function playerTurn() {
  let roll = rollDie();
  while (roll !== 6) {
    console.log(`Player ${currentPlayer + 1} rolled a ${roll}, but didn't get a 6.`);
    currentPlayer = (currentPlayer + 1) % 2; 
    roll = rollDie(); 
  }
  
  movePlayer(currentPlayer, roll);
  currentPlayer = (currentPlayer + 1) % 2; 
}


while (playerPositions[0] < 100 && playerPositions[1] < 100) {
  playerTurn();
}


const winner = playerPositions[0] >= 100 ? 1 : 2;
console.log(`Player ${winner} wins!`);

function move(direction){
    return new Promise(async(resolve,reject)=>{
    if(direction=='up'){
        document.querySelector(`#${turn}`).style.marginTop = String(marginTop() - 9.8) + 'vmin'
    }
    else if(direction=='right'){
        document.querySelector(`#${turn}`).style.marginLeft = String(marginLeft() + 9.8) + 'vmin'
    }
    else if(direction=='left'){
        document.querySelector(`#${turn}`).style.marginLeft = String(marginLeft() - 9.8) + 'vmin'
    }
    await new Promise(resolve => setTimeout(resolve,400))
    resolve()
})
}

function getDirection(){
    let direction
    if((marginLeft()==88.2 && ((((marginTop()*10)%(-19.6*10))/10)==0)) || (marginLeft()==0 && ((((marginTop()*10)%(-19.6*10))/10)!=0))){
        direction = 'up'
    }
    else if((((marginTop()*10)%(-19.6*10))/10)==0){
        direction = 'right'
    }
    else{
        direction = 'left'
    }
    return direction
}

function marginLeft(){
    return Number(document.querySelector(`#${turn}`).style.marginLeft.split('v')[0])
}

function marginTop(){
    return Number(document.querySelector(`#${turn}`).style.marginTop.split('v')[0])
}

function roll(){
    return new Promise(async(resolve,reject)=>{
    let diceNum = Math.floor(Math.random() * 6) + 1
    let values = [[0,-360],[-180,-360],[-180,270],[0,-90],[270,180],[90,90]]
    document.querySelector('#cube_inner').style.transform = 'rotateX(360deg) rotateY(360deg)'
    await new Promise(resolve => setTimeout(resolve,750))
    document.querySelector('#cube_inner').style.transform = `rotateX(${values[diceNum-1][0]}deg) rotateY(${values[diceNum-1][1]}deg)`
    await new Promise(resolve => setTimeout(resolve,750))
    resolve (diceNum)
    })
}