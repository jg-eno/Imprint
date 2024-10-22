import {configureStore} from '@reduxjs/toolkit';
import deckNameSlice from './DeckNameSlice';

const ankiStore = configureStore({reducer:{
    deckNames:deckNameSlice.reducer
}
});

export default ankiStore;

