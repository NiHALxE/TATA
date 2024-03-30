document.addEventListener('DOMContentLoaded', function () {
    const videos = document.querySelectorAll('video');
    videos.forEach(video => {
        video.addEventListener('click', toggleFullScreen);
    });
});

function toggleFullScreen() {
    if (!document.fullscreenElement) {
        this.requestFullscreen().catch(err => {
            console.error('Failed to enter full screen:', err);
        });
    } else {
        document.exitFullscreen();
    }
}
