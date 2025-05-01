import React from 'react';
import '../styles/App.css';

const App = () => {
    return (
        <div className="App">
            <header className="App-header">
                <h1>neon monkey</h1>
                <p>welcome to the chat application!</p>
            </header>
            <main>
                <p>Chat messages will appear here...</p>
                <form>
                    <input type="text" placeholder="Type a message..." />
                    <button type="submit">Send</button>
                </form>
            </main>
            <footer>
                <p>&copy; 2023 neon monkey</p>
            </footer>
        </div>
    );
};

export default App;
