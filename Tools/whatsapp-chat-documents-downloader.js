async function scrollToStart() {
    const applicationElement = document.querySelector('[role="application"]');

    while (!applicationElement?.innerText.includes("Messages are end-to-end encrypted.")) {
        applicationElement.scrollIntoView();
        await new Promise(resolve => setTimeout(resolve, 500));
    }
    console.log("Reached the start of the messages.");
}

async function downloadDocumentsSeenOnWebView() {
    let downloadButtons = Array.from(document.querySelectorAll('[title^="Download "]'));

    if (downloadButtons.length > 0) {
        for (const button of downloadButtons) {
            const filename = button.title.match(/Download\s"(.*)"/)[1];
            console.log(`Downloading: ${filename}`);
            button.click();
            await new Promise(resolve => setTimeout(resolve, 500));
        }
        console.log(`Downloaded ${downloadButtons.length} files.`);
    }
}

async function downloadAllDocumentsInChat() {
    await scrollToStart();
    await downloadDocumentsSeenOnWebView();
}
