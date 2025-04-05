# 🅿️ **Parkon CLI – Visitor Car Registration**
A simple CLI tool for registering guest vehicles visiting your home.

```shell
parkon [command] [options]
```

---

## 📦 Commands

### 🔹 `register` — Register a visitor
Registers a visitor's vehicle on the parkon website and optionally submits the form.

**Usage:**
```shell
parkon register -n NAME [-t DURATION] [-e EMAIL] [-y] [-s] [-i]
```

**Options:**

| Option | Long           | Description                              | Default         |
|--------|----------------|------------------------------------------|-----------------|
| `-n`   | `--name`       | Visitor name                             | *(required)*    |
| `-t`   | `--duration`   | Parking duration (choices: `4`, `8`, `12`, `24`) | `12` |
| `-e`   | `--email`      | Send confirmation email to this address  | from config     |
| `-y`   | `--autosubmit` | Automatically submit the form            | `False`         |
| `-s`   | `--noemail`    | Do not send confirmation email           | `False`         |
| `-i`   | `--headless`   | Run in headless mode (implies autosubmit)| `False`         |

---

### 🔹 `config` — View or change app configuration

**Subcommands:**

#### `show`
Show current configuration values.

```shell
parkon config show
```

#### `set`
Set a configuration key to a new value.

```shell
parkon config set -k KEY -v VALUE
```

**Options:**

| Option | Long     | Description             | Required |
|--------|----------|-------------------------|----------|
| `-k`   | `--key`   | Config key              | ✅       |
| `-v`   | `--value` | New value for the key   | ✅       |

---

### 🔹 `visitor` — Manage stored visitors

**Subcommands:**

#### `show`
Display all registered visitors.

```shell
parkon visitor show
```

#### `add`
Add or update a visitor’s license plate.

```shell
parkon visitor add -n NAME -p PLATE
```

**Options:**

| Option | Long      | Description         | Required |
|--------|-----------|---------------------|----------|
| `-n`   | `--name`  | Visitor name        | ✅       |
| `-p`   | `--plate` | License plate       | ✅       |

#### `delete`
Remove a visitor from the list.

```shell
parkon visitor delete -n NAME
```

**Options:**

| Option | Long     | Description    | Required |
|--------|----------|----------------|----------|
| `-n`   | `--name` | Visitor name   | ✅       |

---

## 🧩 Examples

```shell
# Register a visitor named "alice" for 8 hours
parkon register -n alice -t 8

# Register visitor and automatically submit, no confirmation email
parkon register -n alice -y -s

# Show configuration
parkon config show

# Set default email
parkon config set -k email -v example@email.com

# Add a visitor
parkon visitor add -n bob -p ZH123456

# Delete a visitor
parkon visitor delete -n bob
```

---
