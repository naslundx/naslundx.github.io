function update() {
    let selected = new Set()
    for (let cb of document.querySelectorAll(".filter input:checked")) {
        selected.add(cb.name);
    }

    for (let item of document.querySelectorAll(".container .item")) {
        let categories = new Set(item.classList);
        let intersection = new Set([...selected].filter(x => categories.has(x)));

        if (intersection.size > 0) {
            item.classList.remove("invisible");
        } else {
            item.classList.add("invisible");
        }
    }
}

update();
