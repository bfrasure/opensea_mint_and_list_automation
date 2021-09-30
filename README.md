# opensea_mint_and_list_automation
## Batch Mint and List NFTs on Opensea. This script uses selenium python to automate a chrome driver, 
letting you batch upload and list however many pictures or files as you want.

### This is an open-source project made for the NFT Community
If you want to support this project or me, please check out my NFTs and maybe buy some, i accept most bids.
https://opensea.io/collection/cryptoverse-lone-wanderer

---

# INSTRUCTIONS
1. Download Python and Chrome browser (if you don’t have it already)
2. Download and extract the project in you desired location (note down for future refrence)
3. shift+Rigth click inside project folder and click "open powershell window here" 
4. Pip install requirements.txt (pip install -r requirements.txt)
5. Run the script
6. Fill in all the information in the GUI
7. Press the "Open Browser" button
8. Once the proxy chrome profile is open you can set up your METAMASK wallet (this is a one time set up and as long as you give the same project/repo_save directory the same chrome profile will open)
9. Login to Opensea using your wallet, open the collection you want to upload to and copy the link (note down for future refrence)
10. Press the "Add Item" button on the top right of the webpage and sign the metamask pop up if it appears
11. Make sure all the inputs are correct and click "Run Script"

# Important Notes please read before starting: 
1. Make sure to add the repo_save_location/the project directory before you hit "Open Browser", double check the directory is correct, if it isnt the script will make a new chrome profile where ever you set the directory and the script will most likely crash.
2. Make sure your files are numbered cronologically, the upload loop relies on that heavily
3. If the given upload amount it larger then the amount of files, the script will stop at the upload page after uploading and listing the last file
4. Make sure all the file formats match 
5. The title will be followed by the file number, make sure to leave apropriate spacing at the end of your title if needed(this might change in a future update)

---

If you have any questions or want to get in contact you can find me on instagram and twitter by searching @cloudmaking (feel free to DM).
Huge thank you @Firemarshmellow for continued support with the front end. you can find him on instagram @mellow_fire.
