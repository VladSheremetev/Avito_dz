coverage.init_scroll_markers = function () {
    // Init some variables
    coverage.lines_len = document.querySelectorAll('#source > p').length;

    // Build html
    coverage.build_scroll_markers();
};

coverage.build_scroll_markers = function () {
    const temp_scroll_marker = document.getElementById('scroll_marker')
    if (temp_scroll_marker) temp_scroll_marker.remove();
    // Don't build markers if the window has no scroll bar.
    if (document.body.scrollHeight <= window.innerHeight) {
        return;
    }

    const marker_scale = window.innerHeight / document.body.scrollHeight;
    const line_height = Math.min(Math.max(3, window.innerHeight / coverage.lines_len), 10);

    let previous_line = -99, last_mark, last_top;

    const scroll_marker = document.createElement("div");
    scroll_marker.id = "scroll_marker";
    document.getElementById('source').querySelectorAll(
        'p.show_run, p.show_mis, p.show_exc, p.show_exc, p.show_par'
    ).forEach(element => {
        const line_top = Math.floor(element.offsetTop * marker_scale);
        const line_number = parseInt(element.id.substr(1));

        if (line_number === previous_line + 1) {
            // If this solid missed block just make previous mark higher.
            last_mark.style.height = `${line_top + line_height - last_top}px`;
        } else {
            // Add colored line in scroll_marker block.
            last_mark = document.createElement("div");
            last_mark.id = `m${line_number}`;
            last_mark.classList.add("marker");
            last_mark.style.height = `${line_height}px`;
            last_mark.style.top = `${line_top}px`;
            scroll_marker.append(last_mark);
            last_top = line_top;
        }

        previous_line = line_number;
    });

    // Append last to prevent layout calculation
    document.body.append(scroll_marker);
};

coverage.wire_up_sticky_header = function () {
    const header = document.querySelector('header');
    const header_bottom = (
        header.querySelector('.content h2').getBoundingClientRect().top -
        header.getBoundingClientRect().top
    );

    function updateHeader() {
        if (window.scrollY > header_bottom) {
            header.classList.add('sticky');
        } else {
            header.classList.remove('sticky');
        }
    }

    window.addEventListener('scroll', updateHeader);
    updateHeader();
};

document.addEventListener("DOMContentLoaded", () => {
    if (document.body.classList.contains("indexfile")) {
        coverage.index_ready();
    } else {
        coverage.pyfile_ready();
    }
});
