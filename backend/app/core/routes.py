from fastapi import APIRouter, Depends, Security

import core.router as core_router
import session.router as session_router
import session.security as session_security
import users.router as users_router
import profile.router as profile_router
import activities.router as activities_router
import activity_streams.router as activity_streams_router
import gears.router as gears_router
import followers.router as followers_router
import strava.router as strava_router
import garmin.router as garmin_router
import health_data.router as health_data_router
import health_targets.router as health_targets_router
import websocket.router as websocket_router


router = APIRouter()


# Router files
router.include_router(
    core_router.router,
    tags=["core"],
)
router.include_router(
    session_router.router,
    tags=["session"],
)
router.include_router(
    users_router.router,
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(session_security.validate_access_token)],
)
router.include_router(
    profile_router.router,
    prefix="/profile",
    tags=["profile"],
    dependencies=[
        Depends(session_security.validate_access_token),
        Security(session_security.check_scopes, scopes=["profile"]),
    ],
)
router.include_router(
    activities_router.router,
    prefix="/activities",
    tags=["activities"],
    dependencies=[Depends(session_security.validate_access_token)],
)
router.include_router(
    activity_streams_router.router,
    prefix="/activities/streams",
    tags=["activity_streams"],
    dependencies=[Depends(session_security.validate_access_token)],
)
router.include_router(
    gears_router.router,
    prefix="/gears",
    tags=["gears"],
    dependencies=[Depends(session_security.validate_access_token)],
)
router.include_router(
    followers_router.router,
    prefix="/followers",
    tags=["followers"],
    dependencies=[Depends(session_security.validate_access_token)],
)
router.include_router(
    strava_router.router,
    prefix="/strava",
    tags=["strava"],
)
router.include_router(
    garmin_router.router,
    prefix="/garminconnect",
    tags=["garminconnect"],
    dependencies=[
        Depends(session_security.validate_access_token),
        Security(session_security.check_scopes, scopes=["profile"]),
    ],
)
router.include_router(
    health_data_router.router,
    prefix="/health",
    tags=["health"],
    dependencies=[Depends(session_security.validate_access_token)],
)
router.include_router(
    health_targets_router.router,
    prefix="/health_targets",
    tags=["health_targets"],
    dependencies=[Depends(session_security.validate_access_token)],
)
router.include_router(
    websocket_router.router,
    prefix="/ws",
    tags=["websocket"],
    #dependencies=[
    #    Depends(session_security.validate_access_token),
    #    Security(session_security.check_scopes, scopes=["profile"]),
    #],
)