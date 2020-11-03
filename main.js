// Create a class for the element
class EditableParagraph extends HTMLParagraphElement {
    constructor() { // Always call super first in constructor
        super();
		const defaultVal = this.innerHTML;
		const shadow = this.attachShadow({mode: "open"});
		
		// facio un get all'api del cms
        shadow.innerHTML = defaultVal + " edited";
        shadow.appendChild(div);
    }
}

customElements.define("editable-paragraph", EditableParagraph);
