import { useMemo } from "react";

export function useSource(
  uri: string,
  handler: (event: MessageEvent) => void
): void {
  const source: EventSource = useMemo(() => {
    const src = new EventSource(uri);
    src.addEventListener("message", handler);
    return src;
  }, [uri, handler]);
}
