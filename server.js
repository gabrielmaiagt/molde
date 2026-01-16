const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = process.env.PORT || 9000;

// Firebase Admin Setup
const admin = require('firebase-admin');

try {
    let serviceAccount;
    try {
        serviceAccount = require('./service-account.json');
    } catch (e) {
        console.log('Local service-account.json not found. Using default environment credentials.');
    }

    if (serviceAccount) {
        admin.initializeApp({
            credential: admin.credential.cert(serviceAccount)
        });
    } else {
        admin.initializeApp();
    }
    console.log('Firebase Admin Initialized successfully.');
} catch (error) {
    console.error('Firebase Admin Initialization Error:', error);
}

const MIME_TYPES = {
    '.html': 'text/html',
    '.css': 'text/css',
    '.js': 'text/javascript',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.gif': 'image/gif',
    '.svg': 'image/svg+xml',
    '.ico': 'image/x-icon',
    '.webp': 'image/webp',
    '.woff2': 'font/woff2',
    '.woff': 'font/woff'
};

const server = http.createServer((req, res) => {
    console.log(`Request: ${req.url}`);

    let filePath = '.' + req.url;
    if (filePath === './') {
        filePath = './index.html';
    }

    const extname = path.extname(filePath);
    let contentType = MIME_TYPES[extname] || 'application/octet-stream';

    fs.readFile(filePath, (error, content) => {
        if (error) {
            if (error.code == 'ENOENT') {
                res.writeHead(404);
                res.end('404 Not Found');
            } else {
                res.writeHead(500);
                res.end('Sorry, check with the site admin for error: ' + error.code + ' ..\n');
            }
        } else {
            res.writeHead(200, { 'Content-Type': contentType });
            res.end(content, 'utf-8');
        }
    });
});

server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
});
