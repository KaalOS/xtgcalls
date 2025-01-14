from typing import Dict
from typing import Optional

from ntgcalls import InputMode

from ...ffmpeg import build_ffmpeg_command
from .audio_parameters import AudioParameters
from .audio_stream import AudioStream
from .input_stream import Stream
from .video_parameters import VideoParameters
from .video_stream import VideoStream


class AudioImagePiped(Stream):
    def __init__(
        self,
        audio_path: str,
        image_path: str,
        audio_parameters: AudioParameters = AudioParameters(),
        video_parameters: VideoParameters = VideoParameters(),
        headers: Optional[Dict[str, str]] = None,
        additional_ffmpeg_parameters: str = '',
    ):
        self._image_path = image_path
        self._audio_path = audio_path
        video_parameters.frame_rate = 1
        super().__init__(
            AudioStream(
                InputMode.Shell,
                build_ffmpeg_command(
                    additional_ffmpeg_parameters,
                    self._audio_path,
                    audio_parameters,
                    [],
                    headers,
                ),
                audio_parameters,
            ),
            VideoStream(
                InputMode.Shell,
                build_ffmpeg_command(
                    additional_ffmpeg_parameters,
                    self._image_path,
                    video_parameters,
                    [
                        '-loop',
                        '1',
                        '-framerate',
                        str(video_parameters.frame_rate),
                    ],
                    headers,
                ),
                video_parameters,
            ),
        )
