from pymediainfo import MediaInfo
import os

os.environ["LD_LIBRARY_PATH"] = "usr/local/lib"


def get_audio_info(video_file):
    media_info = MediaInfo.parse(video_file)
    audio_tracks = []
    for track in media_info.tracks:
        if track.track_type == "Audio":
            audio_info = {
                "track_id": track.track_id,
                "language": track.language,
                "codec": track.format,
                "channels": track.channel_s,
            }
            audio_tracks.append(audio_info)
    return audio_tracks
