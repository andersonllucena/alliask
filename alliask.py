const options = {
  method: 'POST',
  headers: {
    'xi-api-key': '26def5525950f5eefcaa3fd0807c0d28',
    'Content-Type': 'application/json'
  },
  body: '{"model_id":"<string>","text":"<string>","voice_settings":{"similarity_boost":123,"stability":123,"style":123,"use_speaker_boost":true}}'
};

fetch('https://api.elevenlabs.io/v1/text-to-speech/CYw3kZ02Hs0563khs1Fj', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
