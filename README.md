# base64_phpinjection
The python script to complement a php injection vuln

The python script takes a user's command and base64 encodes it and sends it to the hard-coded URL.  Change the URL to match your actual target php webapp.  

The snippet of PHP code is what runs your command and returns the system's output.  It needs to be uploaded to the target webapp by the pentester.  

Yes, it can be used to execute a one-line bind or reverse shell.  ;)
