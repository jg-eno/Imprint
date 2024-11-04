import { Link } from "react-router-dom";
import { IoIosArrowDropdown } from "react-icons/io";
import { useState } from "react";
import { useDispatch } from "react-redux";
import { deckNameActions } from "../store/DeckNameSlice";


const DeckNameCard=({name})=>{


  const [editMode,setEditMode]=useState(false);
  const [newDeckName,setNewDeckName]=useState(name);
  const dispatch = useDispatch();


  const handleDeleteDeck=()=>{   

    dispatch(deckNameActions.removeDeckName(name));
    
  };

  const handleClickOnDeck=()=>{
    console.log("Clicked on Deck");
   
  }

  const handleShare=()=>{
    console.log("Share clicked");
  } 

  const handleRename=(e)=>{  
    console.log("Rename clicked");
    e.preventDefault();
    setEditMode(true);
  }

  const handleRenameSubmit = (e) => {
    if (e.key === "Enter") {
      dispatch(deckNameActions.renameDeckName({ oldName: name, newName: newDeckName }));
      setEditMode(false);
    }
  };

  const handleRenameChange = (e) => {
    setNewDeckName(e.target.value);
  };

  return (
    <>
      <div className="deckNameCard">
        <div className="deckNamedisplay" onClick={handleClickOnDeck}>

        {
            editMode ? (
              <input
                type="text"
                value={newDeckName}
                onChange={handleRenameChange}
                onKeyDown={handleRenameSubmit}  // Submits on 'Enter' key
                onBlur={() => setEditMode(false)} // Cancels edit if focus is lost
                className="form-control"
              />
            ) : (
              <Link to="/cardsOfDeck" className="DName">
                {name}
              </Link>
            )
          }
          {/* <Link to="/cardsOfDeck" className='DName'>
            {name}
          </Link> */}
        </div>
         
        <div class="btn-group">
        <button type="button" class="btn btn-success dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
        Action
      </button>
          <ul class="dropdown-menu">
          <li><a class="dropdown-item"  onClick={handleRename}>Rename</a></li>
          <li><a class="dropdown-item" href="#" onClick={handleShare}>Share</a></li>
          <li><a class="dropdown-item" href="#" onClick={handleDeleteDeck}>Delete</a></li>
          </ul>
        </div>
      </div>
    </>
  );
}


export default DeckNameCard;

