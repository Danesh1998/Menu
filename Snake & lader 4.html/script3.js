let turn ='red'
let stopEvent = false
document.querySelector('#red').style.marginLeft = '0vmin'
document.querySelector('#red').style.marginTop = '0vmin'
document.querySelector('#blue').style.marginLeft = '0vmin'
document.querySelector('#blue').style.marginTop = '0vmin'
boxNumbers()

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

function checkWin(){
    if(marginTop()==-88.2 && marginLeft()==0){
        document.querySelector('#p_turn').innerHTML = `${turn}player wins`
        return turn
    }
    else{
        return 'none'
    }
}

function checkRange(diceNum){
    let isOutOfRange = false
    if(marginTop()==-88.2 && (marginLeft()+Number((diceNum*-9.8).toFixed(1)))<0){
        isOutOfRange =true
    }
    return isOutOfRange
}

function changeTurn(){
    if(turn=='blue'){
        document.querySelector('#p_turn').innerHTML = "blue"
        turn = 'red'
    }
    else if(turn=='red'){
        document.querySelector('#p_turn').innerHTML = "red"
        turn = 'blue'
    }
}

function run(diceNum) {
    
    return new Promise(async(resolve,reject)=>{
    for(i=1; i<=diceNum; i++){
      let direction = getDirection()
     await  move(direction)
    } 
    

    checkLadderAndSnakes()
    resolve()
})
}



// Start the game
function playerTurn()
{
    let roll= rollDie();
        while(dicNum !==6) {
            console.log (`Player ${currentplayers +1} rolled a ${dicNum}, but didn't get 6.`);
            currentPlayer = (currentPlayer +1) % 2;
            roll = rollDie();
        
        }
}

function checkLadderAndSnakes(){
    return new Promise(async(resolve,reject)=>{
    // let froms =[[29.4,0],[68.6,-9.8],[68.6,-29.4],[88.2,-39.2],[9.8,-39.2],[58.8,-68.6],[58.8,-19.6],[19.6,-39.2],[58.8,5],[49,-39.2],[78.4,-78.4],[49,-88.2],[49,-58.8],[9.8,-88.2],[0,-29.4]]
    // let tos = [[39.2,-19.6],[49,-39.2],[78.4,-39.2],[78.4,-58.8],[19.6,-58.8],[78.4,-88.2],[39.2,0],[19.6,-9.8],[88.2,-29.4],[39.2,-39.2],[68.6,-49],[29.4,-68.6],[39.2,-39.2][0,-39.2],[19.6,0]]
    let forms =[[29.4,0],[68.6,-9.8],[58.8,-19.6],[68.6,-29.4],[0,-29.4],[9.8,-39.2],[19.6,-39.2],[88.2,-39.2],[58.8,-49],[9.8,-58.8],[49,-58.8],[58.8,-68.6],[39.2,-68.6],[78.4,-78.4],[9.8,-88.2]]
    let tos = [[39.2,-19.6],[49,-39.2],[39.2,0],[78.4,-39.2],[19.6,0],[19.6,-58.8],[19.6,-9.8],[78.4,-58.8],[88.2,-29.4],[0,-78.4],[39.2,-39.2],[78.4,-88.2],[19.6,-49],[68.6,-49],[0,-39.2]]
    for(let i=0; i<tos.length; i++){
        if(marginLeft()==froms[i][0] && marginTop()==froms[i][1]){
            document.querySelector(`#${turn}`).style.marginLeft = `${tos[i][0]}vmin`
            document.querySelector(`#${turn}`).style.marginTop = `${tos[i][1]}vmin`
             await new Promise(resolve => setTimeout(resolve,400))
             break
        }
    }
    resolve()
    } )
}

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
    // var diceNum = Math.floor(Math.random() * 6 + 1);
    // console.log(diceNum)
    // // var img1;

    // switch (diceNum) {

    //     case 1:
             
    //     document.getElementById("#hi").src = "one.png";

    //         break;

    //     case 2:
    //         document.getElementById("#hi").src = "two.png";
    //         break;
    //     case 3:

    //         document.getElementById("#hi").src = "three.png";

    //         break;

    //     case 4:
    //         document.getElementById("#hi").src = "four.png";

    //         break;

    //     case 5:
    //         document.getElementById("#hi").src = "five.png";

    //         break;

    //     case 6:
    //         document.getElementById("#hi").src = "six.png";

    //         break;
    // }

}

function boxNumbers(){
       let boxes = document.querySelectorAll('.box')
       boxes.forEach((box,i)=>{
        if (String(i).length==1 || (String(i).length==2 && Number(String(i)[0]))%2==0){
          //  box.innerHTML = 100-i
        }
        else{
           // box.innerHTML = Number(`${9-Number(String(i)[0])}${String(i)[1]}`)+1
        }
       })
}














































