# octoprintCustomizations
Various scripts and edited config files for customizing OctoPrint/OctoPi
# Camera setting scripts utilizing uvcdynctrl. See https://www.lavrsen.dk/foswiki/bin/view/Motion/SupportQuestion2011x06x30x111729 for details regarding uvcdynctrl options and controls.
## cameraConfig.py
Sets the camera to an initial state:
- Disables auto focus
- Sets absolute focus to 15
- Sets exposure
  - Enables auto exposure
  - Waits 3 seconds for auto exposure to stabilze
  - Enables manual exposure
  - Reads current exposure value 
  - Sets absolute exposure to current value (possibly redundant - might be able to just leave it after enabling manual exposure)
  - Sets saturation to 155
## adjustCameraExposureDecrease.py
Decreases the camera exposure value by 30. Initializes by setting exposure mode to manual, then getting the current exposure value. If statement prevents attempting to send a negative absolute exposure value.
## adjustCameraExposureIncrease.py
Increases the camera exposure value by 30. Initializes by setting exposure mode to manual, then getting the current exposure value. If statement prevents attempting to send an absolute exposure value greater than 280.
## adjustCameraFocusNear.py
Increases the camera focus value by 5, which is the incremental limit for the uvcdynctrl value. Initializes by turning off autofocus, then getting the current exposure value.
## adjustCameraFocusFar.py
Decreases the camera focus value by 5, which is the incremental limit for the uvcdynctrl value. If statement prevents attempting to send an absolute focus value less than 5. Initializes by turning off autofocus, then getting the current exposure value.
## cameraZoomReset.py
Resets the absolute zoom to a value of 100.
## cameraZoomIn.py
Increases the camera absolute zoom by a value of 20. If statement prevents attempting to send an absolute zoom value greater than 180.
## OctoPrint control utilizes the following system controls added to ~/.octoprint/config.yaml
```system:
  actions:
  - name: Initialize Camera
    action: configureCamera
    command: python3 /usr/local/octoprintCustomizations/cameraConfig.py
  - name: Focus Nearer
    action: adjustFocusNear
    command: python3 /usr/local/octoprintCustomizations/adjustCameraFocusNear.py
  - name: Focus Further
    action: adjustFocusFar
    command: python3 /usr/local/octoprintCustomizations/adjustCameraFocusFar.py
  - name: Increase Exposure
    action: adjustExposureIncrease
    command: python3 /usr/local/octoprintCustomizations/adjustCameraExposureIncrease.py
  - name: Decrease Exposure
    action: adjustExposureDecrease
    command: python3 /usr/local/octoprintCustomizations/adjustCameraExposureDecrease.py
  - name: Reset Zoom
    action: zoomReset
    command: python3 /usr/local/octoprintCustomizations/cameraZoomReset.py
  - name: Zoom In
    action: zoomIn
    command: python3 /usr/local/octoprintCustomizations/cameraZoomIn.py 
```
