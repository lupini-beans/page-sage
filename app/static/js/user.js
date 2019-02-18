
const sidebar = $('#sidebar-bg').get(0);
const main = $('#main').get(0);

function toggleSidebar() {
    if (sidebar.style.display === "none") {
        main.style.marginLeft="10%";
        sidebar.style.width="10%";
        sidebar.style.display = "block";
    } else {
        main.style.marginLeft="0%";
        sidebar.style.display = "none";
    }
}
