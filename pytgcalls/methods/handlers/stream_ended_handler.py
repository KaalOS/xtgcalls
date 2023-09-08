from ntgcalls import StreamType

from ...scaffold import Scaffold
from ...types.stream import StreamAudioEnded
from ...types.stream import StreamVideoEnded


class StreamEndedHandler(Scaffold):
    async def _stream_ended_handler(
        self,
        chat_id: int,
        stream: StreamType,
    ):
        await self._on_event_update.propagate(
            'STREAM_END_HANDLER',
            self,
            StreamAudioEnded(
                chat_id,
            ) if stream.Audio else StreamVideoEnded(chat_id),
        )
