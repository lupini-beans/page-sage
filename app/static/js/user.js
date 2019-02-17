
const sidebar = $('#sidebar-bg').get(0);

function toggleSidebar() {
    if (sidebar.style.display === "none") {
        sidebar.style.display = "block";
    } else {
        sidebar.style.display = "none";
    }
}
