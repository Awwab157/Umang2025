const fs = require('fs');
const path = require('path');

const sportsPages = [
    { file: 'basketball.html', sport: 'Basketball', emoji: '🏀', image: 'Vbasketball.png' },
    { file: 'badminton.html', sport: 'Badminton', emoji: '🏸', image: 'Vbadminton.png' },
    { file: 'chess.html', sport: 'Chess', emoji: '♟️', image: 'chess.png' },
    { file: 'kabaddi.html', sport: 'Kabaddi', emoji: '🤼', image: 'kabaddi.png' },
    { file: 'tabletennis.html', sport: 'Table Tennis', emoji: '🏓', image: 'tabletennis.png' },
    { file: 'tennis.html', sport: 'Tennis', emoji: '🎾', image: 'tennis.png' },
    { file: 'throwball.html', sport: 'Throwball', emoji: '⚽', image: 'throwball.png' },
    { file: 'volleyball.html', sport: 'Volleyball', emoji: '🏐', image: 'volleyball.png' }
];

console.log('Ready to update all sports pages with beautiful promotional design!');
console.log('Sports pages to update:', sportsPages.map(s => s.sport).join(', '));