import React, { useState } from 'react';
import '../components/AddCard.css';
import Header from '../components/Header';



const AddCard = () => {
  const [form, setForm] = useState({
    type: '',
    deck: '',
    front: '',
    back: '',
    tags: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm({
      ...form,
      [name]: value,
    });
  };

  const handleSubmit = () => {
    console.log(form);
    // Add form submission logic
  };

  return (
    <>
    <div className="AddCardContainer">
    <Header/>


    <div className="container2">
      <center>
        <div className="Heading">
          Make A New Card
        </div>
      </center>
    <form className='AddcardFrom'>
    
 


  <div class="row mb-3">
    <label for="inputPassword3" class="col-sm-2 col-form-label">Deck</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="DeckName" placeholder='DeckName' />
    </div>
  </div>

  
  <div class="row mb-3">
    <label for="inputPassword3" class="col-sm-2 col-form-label">Front</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="Front" placeholder='Front'/>
    </div>
  </div>


    
  <div class="row mb-3">
    <label for="inputPassword3" class="col-sm-2 col-form-label">Back</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="Back" placeholder='Back'/>
    </div>
  </div>

  <div class="row mb-3">
    <label for="inputPassword3" class="col-sm-2 col-form-label">Tags</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="Tags" placeholder='One or Multiple' />
    </div>
  </div>

  <fieldset class="row mb-3">
    <legend class="col-form-label col-sm-2 pt-0">Type:</legend>
    <div class="col-sm-10">
      <div class="form-check">
        <input class="form-check-input" type="radio" name="gridRadios" id="gridRadios1" value="option1" checked />
        <label class="form-check-label" for="gridRadios1">
          Basic
        </label>
      </div>
      <div class="form-check">
        <input class="form-check-input" type="radio" name="gridRadios" id="gridRadios2" value="option2" />
        <label class="form-check-label" for="gridRadios2">
          Optional
        </label>
      </div>
      
    </div>
  </fieldset>

  
  <button type="submit" class="AddCardButton btn btn-primary">Add Card</button>
</form>
    </div>
    </div>
    </>
  );
};

export default AddCard;
