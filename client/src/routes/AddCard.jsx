import React, { useRef, useState } from "react";
import "../components/AddCard.css";
import Header from "../components/Header";

const AddCard = () => {

  const [notification, setNotification] = useState("");
  const [options, setOptions] = useState([]);

  const deckNameRef = useRef("");
  const frontRef = useRef("");
  const backRef = useRef("");
  const tagsRef = useRef("");

  const [mcq, setMcq] = useState(false);
  const [generatedMCQ, setGeneratedMCQ] = useState(null);

  const handleSubmit = () => {
    const deckNamevalue = deckNameRef.current.value;
    const frontvalue = frontRef.current.value;
    const backvalue = backRef.current.value;
    const tagsValue = tagsRef.current.value;

    console.log(deckNamevalue);
    deckNameRef.current.value = "";
    frontRef.current.value = "";
    backRef.current.value = "";
    tagsRef.current.value = "";

    setNotification(`Card added successfully!`);
    setTimeout(() => {
      setNotification('');
    }, 3000);
  };

  const handleMcq = () => {
    console.log("MCQ");
    setMcq(true);
  };

  const handleBasic = () => {
    console.log("Basic");
    setMcq(false);
  };

  // const handleGenerate = () => {
  //   console.log("Generate");
   
  // };
  

  const handleGenerate = async () => {
    try {
      const question = frontRef.current.value; // Use the front value as the question
      const answer=backRef.current.value; // Use the back value as the answer
      // Send POST request to your backend
      const response = await fetch("http://127.0.0.1:5000/alternative", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question ,answer}),
      });

      if (!response.ok) throw new Error("Failed to fetch MCQ");

      const mcqData = await response.json();

      setGeneratedMCQ(mcqData); // Save generated MCQ data in state for display
      console.log(mcqData);
      console.log(mcqData.Options);
      setOptions(mcqData.Options);

     
    
      setNotification("MCQ generated successfully!");
      setTimeout(() => {
        setNotification('');
      }, 3000);
    } catch (error) {
      console.error("Error generating MCQ:", error);
      setNotification("Failed to generate MCQ. Please try again.");
      setTimeout(() => {
        setNotification('');
      }, 3000);
    }
  };

  const handleApproveAll = () => { }
  const handleDisapproveAll = () =>{}

  return (
    <>
      <div className="AddCardContainer">
        <Header />
        {notification && <div className="notification">{notification}</div>}

        <div className="container2">
          <center>
            <div className="Heading">Make A New Card</div>
          </center>
          <div className="AddcardFrom">
            <div class="row mb-3">
              <label for="inputPassword3" class="col-sm-2 col-form-label">
                Deck
              </label>
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control"
                  id="DeckName"
                  placeholder="DeckName"
                  ref={deckNameRef}
                />
              </div>
            </div>

            <div class="row mb-3">
              <label for="inputPassword3" class="col-sm-2 col-form-label">
                Front
              </label>
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control"
                  id="Front"
                  placeholder="Front"
                  ref={frontRef}
                />
              </div>
            </div>

            <div class="row mb-3">
              <label for="inputPassword3" class="col-sm-2 col-form-label">
                Back
              </label>
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control"
                  id="Back"
                  placeholder="Back"
                  ref={backRef}
                />
              </div>
            </div>

            <div class="row mb-3">
              <label for="inputPassword3" class="col-sm-2 col-form-label">
                Tags
              </label>
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control"
                  id="Tags"
                  placeholder="One or Multiple"
                  ref={tagsRef}
                />
              </div>
            </div>

            <fieldset class="row mb-3">
              <legend class="col-form-label col-sm-2 pt-0">Type:</legend>
              <div class="col-sm-10">
                <input
                  type="radio"
                  className="btn-check"
                  name="options-outlined"
                  id="success-outlined"
                  autocomplete="off"
                  checked
                />
                <label
                  className="b btn btn-outline-info"
                  for="success-outlined"
                  onClick={handleBasic}
                >
                  Basic
                </label>

                <input
                  type="radio"
                  className="btn-check"
                  name="options-outlined"
                  id="danger-outlined"
                  autocomplete="off"
                />
                <label
                  className="b btn btn-outline-danger"
                  for="danger-outlined"
                  onClick={handleMcq}
                >
                  MCQ
                </label>
              </div>
            </fieldset>

            {mcq && (
              <div className="generateWithAI">
                <button className="generate-btn" onClick={handleGenerate}>
                  Generate with AI
                </button>
              </div>
            )}

            {mcq && options.length > 0 && (
              <div className="mcq-container">
                
                <div className="mcq-options">
                  {options.map((x, index) => (
                    <div className="mcq-option" key={index}>
                      {x}
                    </div>
                  ))}
                </div> 
                <div className="mcq-actions">
                  <button className="mcq-button approve" onClick={handleApproveAll}>Approve All</button>
                  <button className="mcq-button disapprove" onClick={handleDisapproveAll}>Disapprove All</button>
                </div>               
              </div>
            )}
            <button
              type="submit"
              class="AddCardButton btn btn-primary"
              onClick={handleSubmit}
            >
              Add Card
            </button>
          </div>
        </div>
      </div>
    </>
  );
};

export default AddCard;
