# Command menu: cmdk

Chưa dùng project nào, đề xuất cho app nhiều route/action (chia-keo, mytools
style command palette — mytools đã có `CommandMenu.tsx` riêng, tham khảo được).

```
pnpm add cmdk
```

```tsx
import { Command } from "cmdk";

function CommandMenu({ open, onOpenChange }: { open: boolean; onOpenChange: (v: boolean) => void }) {
  return (
    <Command.Dialog open={open} onOpenChange={onOpenChange} label="Command Menu">
      <Command.Input placeholder="Tìm hoặc gõ lệnh..." />
      <Command.List>
        <Command.Empty>Không tìm thấy.</Command.Empty>
        <Command.Group heading="Điều hướng">
          <Command.Item onSelect={() => {/* navigate */}}>Trang chủ</Command.Item>
        </Command.Group>
      </Command.List>
    </Command.Dialog>
  );
}
```

Unstyled hoàn toàn — tự viết CSS/Tailwind cho `[cmdk-*]` selector. Bind
`⌘K`/`Ctrl+K` mở bằng `useEffect` + `keydown` listener riêng, cmdk không tự
làm việc đó.

## Lựa chọn khác (không dùng)

- **kbar** — có sẵn UI mặc định đẹp hơn, ít công tự style, nhưng bundle to hơn
  và khó custom sâu bằng cmdk.

## Cách đổi lib sau này

Nên bọc trong 1 component `CommandMenu` riêng (như mytools đã làm), chỗ khác
chỉ gọi `<CommandMenu />` — đổi lib chỉ sửa trong file đó.
