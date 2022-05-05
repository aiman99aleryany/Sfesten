# Project brief:
<p>This project will aim at creating QR codes for the following data types:</p>
<ol>
<li>Vcards.</li>
<li>Web links.</li>
<li>Code encryption algorithms.</li>
<li>Images jpg, png, gif.</li>
<li>Windows Executable program.</li>
<li>Geo location.</li>
<li>Mp3 audio files.</li>
<li>Pdf documents.</li>
<li></li>
</ol>

<h3>Technologies used in project:</h3>
<p>This project is a pure Python project and will be integrated with sqlite3 and django later on, with some addition by ducker to be compatible on all systems.</p>

<h3>New things expected to be learned and practiced on this project:</h3>

<ol>
<li>Dunder Methods.</li>
<li>Decorators.</li>
<li>Databases.</li>
<li>Django.</li>
<li>Web sockets.</li>
<li>OOP.</li>
<li>Modules: requests, os, pathlib, sys, pyinputplus, pyperclip, timeit, sqlite3, unittest, random, qrcode, regex, tkinter</li>
<li>Encryption Algorithms.</li>
</ol>

<h2>Project Stages:</h2>

<ul>

<li>Choosing the data type from the user, what is the data type that will be converted to qr code.</li>

<li>The Requirements will change according to the data type chosen.</li>

<li>Fetching the Requirements/data from the user by pointing the path whether it's a vcard, pdf or image etc. Or you can enter the data manually.</li>

<li>Compare if all the provided data fits the chosen data type, by accessing the data type models. and if it fits will continue to the next stage.</li>

<li>Creating the QR code.</li>

<li>Show the QR code to the user and deliver it in JPG form.</li>

<li>Add a foreign key to the QR code to be added to the database.</li>

<li>The database will be transferred to the django server. </li>

<li>You will be able to search for the qr code by the foreign key on the server.</li>

<li>Later improvements can be added to the server, so you can generate a qr code from the django server directly. And you can see how many scans has occurred on each QR code.</li>

</ul>


<p>What should be done:</p>

<ol>
part 1
<ul>
    <li> Create the flow chart</li>
    <li> Identify the type of the information that needs to be converted. </li>
    <li> Take the information we need in order to create the QR code. 
</li>
    <li> Create the QR code. </li>
    <li>Send the QR code to the requester by email. </li>
    <li>Save the QR code at the database along with the email. </li>
</ul>
<br>
part 2
<ul>
    <li> You should be able to read the QR code. </li>
    <li> You should have an option to encrypt the QR code. </li>

</ul>
</ol>





