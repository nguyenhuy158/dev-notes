# State client nhẹ: zustand

Chưa dùng project nào. Dùng khi cần share state UI cross-component mà
TanStack Query (server state) hoặc React Context (ít re-render) không hợp —
ví dụ state UI tạm như sidebar collapsed, filter đang chọn, wizard step.

```
pnpm add zustand
```

```ts
import { create } from "zustand";

type UIState = {
  sidebarCollapsed: boolean;
  toggleSidebar: () => void;
};

export const useUIStore = create<UIState>((set) => ({
  sidebarCollapsed: false,
  toggleSidebar: () => set((s) => ({ sidebarCollapsed: !s.sidebarCollapsed })),
}));
```

```tsx
const collapsed = useUIStore((s) => s.sidebarCollapsed);
```

Không cần Provider, không boilerplate action/reducer. Persist qua
`localStorage` dùng middleware `zustand/middleware` (`persist(...)`) — mytools
hiện tự tay đọc/viết `localStorage` trong `useEffect`, zustand persist gọn
hơn nếu refactor sau.

## Lựa chọn khác (không dùng)

- **jotai** — atomic, hợp state nhỏ lẻ nhiều nơi độc lập; zustand hợp hơn khi
  state gom thành 1-vài store rõ ràng.
- **React Context + useReducer** — không cần thêm dependency, nhưng re-render
  toàn subtree khi state đổi trừ khi tách context kỹ; zustand tránh vấn đề này
  bằng selector.

## Cách đổi lib sau này

Store định nghĩa tập trung 1 file (`store/xxx.ts`), nơi dùng chỉ gọi hook
`useXxxStore(selector)` — đổi lib chỉ sửa trong file store.
