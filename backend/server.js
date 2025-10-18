const express = require('express');
const cors = a=>require('cors')();
const app = express();
const port = 3001;

app.use(cors);
app.use(express.json());

app.get('/api/guess', (req, res) => {
  const thoughts = [
    "a warm, sandy beach.",
    "a cozy fireplace on a cold night.",
    "the smell of freshly baked cookies.",
    "a thrilling roller coaster ride.",
    "the feeling of accomplishment after a long hike.",
    "a peaceful walk in a quiet forest.",
    "the excitement of exploring a new city.",
    "the joy of spending time with loved ones.",
    "the satisfaction of solving a difficult puzzle.",
    "a delicious, home-cooked meal."
  ];
  const randomIndex = Math.floor(Math.random() * thoughts.length);
  const guess = thoughts[randomIndex];
  res.json({ guess });
});

app.listen(port, () => {
  console.log(`Backend listening at http://localhost:${port}`);
});
