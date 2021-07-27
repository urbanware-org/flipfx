# *FlipFX*

**Table of contents**
*   [Definition](#definition)
*   [Details](#details)
*   [Requirements](#requirements)
*   [Contact](#contact)
*   [Useless facts](#useless-facts)

----

## Definition

The *FlipFX* module allows printing a string with a flipping character effect.

:keyboard: If you are interested in a typewriter effect text printer module, you can find it [here](https://github.com/urbanware-org/typefx).

:left_right_arrow: There also is a left-to-right line bouncing effect module [here](https://github.com/urbanware-org/bouncefx).

[Top](#flipfx)

## Details

Before the given string is printed, a random one with the same length will be created and printed. With a user-defined delay the characters will flip randomly until all of them are identical with the given one.

### Usage

First of all, the module must be imported.

```python
import flipfx
```

#### Method

Notice that the delay must be given in milliseconds.

The method requires only two arguments, the string that should be printed and the delay between flipping the characters:

```python
flipfx.charflip(string, delay=80)
```

#### Example

The following code

```python
import flipfx
flipfx.charflip("This is an example how the module works.", 80)
```

produces this output:

<img src="https://raw.githubusercontent.com/urbanware-org/flipfx/master/gif/flipfx.gif" alt="FlipFX sample output">

[Top](#flipfx)

## Requirements

In order to use *FlipFX*, the *Python* framework must be installed on the system.

Depending on which version of the framework you are using:

*   *Python* 2.x (version 2.7 or higher is recommended, may also work with earlier versions)
*   *Python* 3.x (version 3.2 or higher is recommended, may also work with earlier versions)

[Top](#flipfx)

## Contact

Any suggestions, questions, bugs to report or feedback to give?

You can contact me by sending an email to [dev@urbanware.org](mailto:dev@urbanware.org) or by opening a *GitHub* issue (which I would prefer if you have a *GitHub* account).

[Top](#flipfx)

## Useless facts

*   The project name is an abbreviation for *Flip Effects*.

[Top](#flipfx)
