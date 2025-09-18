document.addEventListener("DOMContentLoaded", () => {
    const deviceInfo = {
        UserAgent: navigator.userAgent,
        Platform: navigator.platform,
        longitude: null,
        latitude: null
    }

    console.log(deviceInfo)
    const deviceInfoField = document.getElementById('deviceInfo')
    if (!deviceInfoField) {
        console.error("No Field found")
        return
    }

    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition((data) => {
            console.log(data, 'data')
            deviceInfo.longitude = data.coords.longitude
            deviceInfo.latitude = data.coords.latitude
        }, (error) => {
            switch(error.code) {
                case error.PERMISSION_DENIED:
                    console.error("User denied permission", {error})
                    break;
                case error.POSITION_UNAVAILABLE:
                    console.error("Position is unavailable", { error })
                    break;
                case error.TIMEOUT:
                    console.log("getting location timed out.", {error})
            }
        }, { enableHighAccuracy: true, timeout: 3000, maximumAge: 0 })
    }

    deviceInfoField.value = JSON.stringify(deviceInfo)
})