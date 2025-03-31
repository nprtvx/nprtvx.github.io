// src/pages/Home.js
import React from 'react';
import NavBar from '../components/NavBar.js';
import ChatsSection from '../components/ChatsSection.js';
import ChatScreen from '../components/ChatScreen.js';

/*

import styled from './styled-components.js';

const HomeContainer = styled.div`
  display: flex;
  flex-direction: column;
  height: 100vh;
`;

const MainContent = styled.div`
  display: flex;
  flex: 1;
  overflow: hidden;
`;

*/

const Home = () => {
  return (
    <>
    <p>welcome to neon monkey</p>
    <img src="../../../public/media/logo.svg" alt="logo"/>
    <img src="../../../public/media/Another.svg" alt="logo"/>
    <p>just a test site</p>

    </>
  );
};

/*

<HomeContainer>
      <NavBar />
      <MainContent>
        <h2>welcome to all the enthusiasts</h2>
        <ChatsSection />
        <ChatScreen />
      </MainContent>
    </HomeContainer>

*/

export default Home;