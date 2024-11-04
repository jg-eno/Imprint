import Header2 from "../components/Header2";
import "../components/CardOfDecks.css";
import { useState } from "react";

const CardsOfDecks = () => {
  const [count, setCount] = useState(0); 
  const [showAnswer, setShowAnswer] = useState(false); 

  const increment = () => setCount(count + 1);
  const decrement = () => setCount(count - 1);

  const [isFlipped, setIsFlipped] = useState(false);

  
  // Function to handle the flip
  const handleFlip = () => {
    setIsFlipped(!isFlipped);
  };


  const handleEdit=()=>{
    console.log("Edit");
    window.location.href = "/addcard";
  }


  const handleLimits = () => { 
    console.log("Limits");
    window.location.href = "/setLimits";

  }

  const front = "Formula for sin(2x)";
  const back = "sin(2x) = 2sin(x)cos(x)";

  return (
    <>
      <div className="CardsOfDeckContainer">
        <Header2 />

        <div className="flashcard-container">
          <div className="headerss">
            <div className="leftHeaderss">
              <button className="hButtons btn btn-outline-primary"
                onClick={handleEdit}>Edit</button>
              <button className="hButtons btn btn-outline-primary"
              onClick={handleLimits}>
                Limits
              </button>

              <button
                className=" hButtons btn btn-outline-primary"
                onClick={increment}
              >
                +
              </button>
              <button
                className="hButtons btn btn-outline-primary"
                onClick={decrement}
              >
                -
              </button>
            </div>

            <div className="counter">{count} + 1 + 1</div>
          </div>

          <div
            className={`card ${isFlipped ? "flipped" : ""}`}
            onClick={handleFlip}
          >
            <div className="card-inner">
              <div className="front card-front">
                <p className="frontQuestion">{front}</p>
              </div>
              <div className="back card-back">
                <p>{back}</p>
              </div>
            </div>
          </div>

         

          {isFlipped == true ? (
            <div class="button-container">
              <div class="button-item">
                <span> 1m</span>
                <button>Again</button>
              </div>
              <div class="button-item">
                <span>6m</span>
                <button>Hard</button>
              </div>
              <div class="button-item">
                <span>10m</span>
                <button>Good</button>
              </div>
              <div class="button-item">
                <span>5d</span>
                <button>Easy</button>
              </div>
            </div>
          ) : (
            <div></div>
          )}

          {/* <div className="showAnswerButton">
      {

      showAnswer ==false?
      <button type="button" className="showAnswerButton btn btn-primary btn-lg" onClick={() => setShowAnswer(!showAnswer)}>
      Show Answer
      </button>:
      <button type="button" className="showAnswerButton btn btn-primary btn-lg" onClick={() => setShowAnswer(!showAnswer)}>
      Hide Answer
      </button>

      }
      </div> */}

      
        </div>
      </div>
    </>
  );
};

export default CardsOfDecks;
