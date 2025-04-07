import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './App';

try {
    const container = document.getElementById("root");
    if (container) {
        const root = ReactDOM.createRoot(container);
        root.render(
            <React.StrictMode>
                <BrowserRouter>
                    <App />
                </BrowserRouter>
            </React.StrictMode>
        );
    } else {
        throw new Error('Root container not found');
    }
} catch (error) {
    console.error('Failed to render the application:', error);
}
