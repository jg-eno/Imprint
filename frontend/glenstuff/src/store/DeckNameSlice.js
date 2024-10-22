import {createSlice} from '@reduxjs/toolkit';

const deckNameSlice = createSlice({
          name:"deckNames",
          initialState:[],
          reducers:{
              addDeckName(state,action){
                  console.log("Deck Name:", action.payload);
                  state.push(action.payload);
                  console.log("No of values in DeckName Store:", state.length);
              },
              removeDeckName(state, action) {
                  console.log("Deck Name:", action.payload);
                  const index = state.findIndex(deckName => deckName === action.payload);
                  if (index !== -1) {
                      state.splice(index, 1);
                  }
                  console.log("No of values in DeckName Store:", state.length);
              }
          }
});


export const deckNameActions = deckNameSlice.actions;

export default deckNameSlice; 
