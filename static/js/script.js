// import { API_KEY } from './configure.js';

document.addEventListener('DOMContentLoaded', function() {
  
  // const axios = require("axios").default;
  
  const refreshInterval = 5000;
    
  // const assembly = axios.create({
  //   baseURL: "https://api.assemblyai.com/v2",
  //   headers: {
  //     authorization: API_KEY,
  //     "content-type": "application/json",
  //   },
  // });
  
  // const getTranscript = async () => {
  //   const response = await assembly.post("/transcript", {
  //     audio_url: audioURL,
  //   });
  
  var intervalId = window.setInterval(function(){
    fetch('/transcribe')
    .then(response => response.json())
    .then(data => {
      console.log('GET response:');
      console.log(data); 
      console.log(data.text)
      if (data.audio_duration != null){
        clearInterval(intervalId)
        document.getElementById('transcript_text').innerHTML = data.text;
      }
    });

  }, refreshInterval);
  
//   const checkCompletionInterval = setInterval(async () => {
//     const transcript = await assembly.get(`/transcript/${response.data.id}`);
//     const transcriptStatus = transcript.data.status;
  
//     if (transcriptStatus === "completed") {
//       let transcriptText = transcript.data.text;
//       document.getElementByName("results").innerText = transcriptText;
//       clearInterval(checkCompletionInterval);
//     }
//   }, refreshInterval);
  
//   // getTranscript();
//   checkCompletionInterval();
})



