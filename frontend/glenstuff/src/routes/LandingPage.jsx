import React, { useState,useRef } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import {useDispatch} from 'react-redux';
import { deckNameActions } from '../store/DeckNameSlice';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';
import DeckNameCard from '../components/DeckNameCard';

const LandingPage = () => {


  const [isModalOpen, setIsModalOpen] = useState(false);
  const [notification, setNotification] = useState('');
  const [viewDeck,setViewDeck]=useState(false);
  
  const deckNameRef = useRef(null);

  const dispatch=useDispatch();
  const handleCreateNewDeck = () => {
    // console.log("create new deck is clicked");
    setIsModalOpen(true);
  };

  
  
  const handleInputChange = (e) => {
    // console.log("Deck Name:", e.target.value);
  };


  const handleSubmit = (e) => {    
    console.log("Deck Name:", deckNameRef.current.value);
    setIsModalOpen(false);
    setNotification(`Deck "${deckNameRef.current.value}" created successfully!`);



    dispatch(deckNameActions.addDeckName(deckNameRef.current.value));
    deckNameRef.current.value = '';
    


    console.log(deckItems)

    setTimeout(() => {
      setNotification('');
    }, 3000);
    
  };


  const deckItems=useSelector((store)=>store.deckNames)


  const handleDelete = (e) => {

    dispatch(deckNameActions.removeDeckName(deckNameRef.current.value));
    setIsModalOpen(false);

  };


  const handleViewDecks = () => {
    // console.log("View Decks is clicked");
    if(deckItems.length==0){
      setNotification("No Decks to display");
      setTimeout(() => {
        setNotification('');
      }, 3000);
    }
    else{
      setViewDeck(true);
    }
  };


  return (
    <>
      <div className="landing-container2">
        <Header />
        <div className="landing-container">
          <div className="welcome-box">
          <h2 className="welcome-title">
            Welcome to Your 
           <br />
            Personal Flashcard Hub
          </h2>
          <h5 className="subtitle">
            Create, customize, and conquer your learning with personalized flashcards!
          </h5>

            <div className="action-buttons">
              <button
                type="button"
                className="create-button btn btn-outline-primary"
                onClick={handleCreateNewDeck}
              >
                Create New Deck
              </button>

              {
                viewDeck == false ?
              <button
                type="button"
                className="view-button btn btn-outline-success"
                onClick={handleViewDecks}
              >
                View Decks
              </button>:
              <button
                type="button"
                className="view-button btn btn-outline-danger"
                onClick={()=>setViewDeck(false)}
              >
                Hide Decks
              </button>

              }
            </div>
            {isModalOpen && (
              

              <div className="random">
             
                <div class="col">
                <input type="text" 
                class="form-control" 
                placeholder="Enter DeckName:"                
                ref={deckNameRef}
                onChange={handleInputChange}/>
                <button type="button" class="btn k btn-primary btn-sm" onClick={handleSubmit}>Add Deck</button>
                <button type="button" class="btn k btn-secondary btn-sm" onClick={handleDelete}>Delete</button>
              </div>
              </div>
            
              )}

              {notification && (
                  <div className="notification">
                    {notification}
                  </div>
              )}

              {
               viewDeck &&
                deckItems.map((ITM)=>(
                  <DeckNameCard name={ITM} key={ITM}>

                  </DeckNameCard>
                  
                ))
              }

              {
                viewDeck && deckItems.length==0 &&
                <div className="notification">
                  No Decks to display
                </div>
              }
              
            
          </div>
        </div>
       
        <Footer />
      </div>
      
    </>
  );
};

export default LandingPage;
