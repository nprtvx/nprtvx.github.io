// src/pages/Home.js
import React from 'react';
import NavBar from '../components/NavBar';
import ChatsSection from '../components/ChatsSection';
import ChatScreen from '../components/ChatScreen';
import styled from 'styled-components';

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

const Home = () => {
  return (
    <HomeContainer>
      <NavBar />
      <MainContent>
        <ChatsSection />
        <ChatScreen />
      </MainContent>
    </HomeContainer>
  );
};

export default Home;